# -*- coding: utf-8 -*-
import os
import bz2
from ..serialization import JsonWrapper
from .. import config, Database, databases


class DatabaseExport(object):
    """Export database to Brightway2 format, which is bz2-compressed JSON. Pickle can't be used because of security reasons.

    Brightway2 format for databases is:

    .. code-block::

        {
            "meta":
                {
                "name": database_name,
                "depends": [list_of_databases],
                "version": version_number,
                "from format": format,
                "bw2 version": bw2_version
                },
            "data": [
                [database_name, process_id], [process_data],
                ]
        }

    """
    def exporter(self, name):
        """Export a database to Brightway2 format.

        Args:
            *name* (str): Name of database to export.

        Returns:
            Filepath of exported database.

        """
        assert name in databases, "Database %s not found" % name
        meta = databases[name]
        data = Database(name).load().iteritems()
        version = config.version
        processed = {
            "meta": {
                "name": name,
                "depends": meta["depends"],
                "version": meta["version"],
                "from format": meta["from format"],
                "bw2 version": version
                },
            "data": data
            }
        dirname = config.request_dict("export")
        assert dirname, "No suitable directory for export found"
        filepath = os.path.join(dirname, name + ".json.bz2")
        with bz2.BZ2File(filepath, "w") as f:
            f.write(JsonWrapper.dumps(processed))
        return filepath
