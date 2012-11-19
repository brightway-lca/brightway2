# -*- coding: utf-8 -*-
from .. import Database
from ..logs import get_io_logger
from ..serialization import JsonWrapper
from ..validate import db_validator
import bz2
import os


class DatabaseImporter(object):
    def importer(self, path):
        data = JsonWrapper.loads(bz2.BZ2File(path, "r").read())
        for o in data:
            # Do validation of all incoming data first
            db_validator(o["data"])
        logger, logfile = get_io_logger(os.get_filename(path))
        report_needed = sum([self.update_database(
            o["data"], o["meta"], logger) for o in data])
        return report_needed, logfile

    def update_database(self, data, meta, logger):
        name = meta["name"]
        try:
            old = Database(name)
            odata = old.load()
        except IOError:
            # Create new database
            database = Database(name)
            database.register(
                format="Brightway2 internal",
                depends=meta["depends"],
                num_processes=len(data))
            database.write(data)
            database.process()
            # No messages about this import
            logger.info(u"Database %s created" % name)
            return False

        # First, see if data will be overwritten
        if self.no_difference(odata, data):
            logger.debug(u"DEBUG: Database %s not changed" % name)
            return False

        # There are changes to be made; log them
        for message in self.get_changes(odata, data):
            logger.info(message)

        # Finally, update data
        odata.update(**data)
        old.write(odata)
        old.process()
        return True

    def no_difference(self, d, e):
        """Test if ``d`` properly contains ``e``.

        Note that ``d`` can have *more* than ``e``."""
        for key in e:
            if key in d and d[key] == e[key]:
                continue
            else:
                return False
        return True

    def get_changes(self, old, new):
        messages = []
        for key in new:
            if key not in old:
                messages.append(u"Process %s (%s) added" % (
                    new[key]["name"], key))
            elif new[key] == old[key]:
                continue
            else:
                attrs = []
                for attr in new[key]:
                    if new[key][attr] != old[key].get(attr, None):
                        attrs.append(attr)
                assert attrs
                messages.append(u"Process %s update the following:\n\t%s" % (
                    new[key]["name"], u", ".join(attrs)))

        return messages
