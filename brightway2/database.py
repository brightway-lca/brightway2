# -*- coding: utf-8 -*-
from . import databases, config, mapping
from errors import MissingIntermediateData, UnknownObject
from query import Query
from time import time
from utils import natural_sort, MAX_INT_32
from validate import db_validator
import datetime
import numpy as np
import os
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Database(object):
    """A manager for a database. This class can register or deregister databases, write intermediate data, process data to parameter arrays, query, validate, and copy databases.

    Databases are automatically versioned.

    The Database class never holds intermediate data, but it can load or write intermediate data. The only attribute is *database*, which is the name of the database being managed.

    Instantiation does not load any data. If this database is not yet registered in the metadata store, a warning is written to ``stdout``.

    Args:
        *database* (str): Name of the database to manage.

    """
    def __init__(self, database):
        """Instantiate a Database object.

        Does not load any data. If this database is not yet registered in the metadata store, a warning is written to **stdout**.


        """
        self.database = database
        if self.database not in databases:
            print "Warning: %s not a currently installed database" % database

    @property
    def version(self):
        """The current version number (integer) of this database.

        Returns:
            Version number

        """
        return databases.version(self.database)

    def query(self, *queries):
        """Search through the database. See :class:`query.Query` for details."""
        return Query(*queries)(self.load())

    def relabel_data(self, data, new_name):
        """Relabel database keys and exchanges.

        In a database which internally refer to the same database, update to new database name ``new_name``.

        Needed to copy a database completely or cut out a section of a database.

        For example:

        .. code-block:: python

            data = {
                ("old and boring", 1):
                    {"exchanges": [
                        {"input": ("old and boring", 42),
                        "amount": 1.0},
                        ]
                    },
                ("old and boring", 2):
                    {"exchanges": [
                        {"input": ("old and boring", 1),
                        "amount": 4.0}
                        ]
                    }
                }
            print relabel_database(data, "shiny new")
            >> {
                ("shiny new", 1):
                    {"exchanges": [
                        {"input": ("old and boring", 42),
                        "amount": 1.0},
                        ]
                    },
                ("shiny new", 2):
                    {"exchanges": [
                        {"input": ("shiny new", 1),
                        "amount": 4.0}
                        ]
                    }
                }

        In the example, the exchange to ``("old and boring", 42)`` does not change, as this is not part of the updated data.

        Args:
            * *data* (dict): The database data to modify
            * *new_name* (str): The name of the modified database

        Returns:
            The modified database

        """
        def relabel_exchanges(obj, new_name):
            for e in obj['exchanges']:
                if e["input"] in data:
                    e["input"] = (new_name, e["input"][1])
            return obj

        return dict([((new_name, k[1]), self.relabel_exchanges(v, new_name)) \
            for k, v in data.iteritems()])

    def copy(self, name):
        """Make a copy of the database.

        Internal links within the database will be updated to match the new database name.

        Args:
            * *name* (str): Name of the new database.

        """
        assert name not in databases, ValueError("This database exists")
        data = self.relabel_data(self.load(), name)
        new_database = Database(name)
        new_database.register(
            format="Brightway2 copy",
            depends=databases[self.database]["depends"],
            num_processes=len(data))
        new_database.write(data)

    def backup(self):
        """Save a backup to ``backups`` folder.

        Returns:
            Filepath of backup.

        """
        filepath = os.path.join(config.request_dir("backups"), self.filename() + \
            ".%s.backup" % int(time()))
        with open(filepath, "wb") as f:
            pickle.dump(self.load(), f, protocol=pickle.HIGHEST_PROTOCOL)
        return filepath

    def revert(self, version):
        """Return data to a previous state.

        .. warning:: Reverted changes can be overwritten.

        Args:
            * *version* (int): Number of the version to revert to.

        """
        assert version in [x[0] for x in self.versions()], "Version not found"
        self.backup()
        databases[self.database]["version"] = version
        self.process(version)

    def register(self, format, depends, num_processes):
        """Register a database with the metadata store.

        Databases must be registered before data can be written.

        Args:
            * *format* (str): Format that the database was converted from, e.g. "Ecospold"
            * *depends* (list): Names of the databases that this database references, e.g. "biosphere"
            * *num_processes* (int): Number of processes in this database.

        """
        assert self.database not in databases
        databases[self.database] = {
            "from format": format,
            "depends": depends,
            "number": num_processes,
            "version": 0
            }

    def deregister(self):
        """Remove a database from the metadata store. Does not delete any files."""
        del databases[self.database]

    def validate(self, data):
        """Validate data. Must be called manually.

        Raises ``voluptuous.Invalid`` if data does not validate.

        Args:
            * *data* (dict): The data, in its processed form.

        """
        db_validator(data)

    def filename(self, version=None):
        """Filename for given version; Default is current.

        Returns:
            Filename (not path)

        """
        return "%s.%i.pickle" % (self.database,
            version or self.version)

    def write(self, data):
        """Serialize data to disk.

        Args:
            * *data* (dict): Inventory data

        """
        if self.database not in databases:
            raise UnknownObject("This database is not yet registered")
        databases.increment_version(self.database)
        mapping.add(data.keys())
        filepath = os.path.join(config.dir, "intermediate", self.filename())
        with open(filepath, "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, version=None):
        """Load the intermediate data for this database.

        Can also load previous versions of this database's intermediate data.

        Args:
            * *version* (int): Version of the database to load. Default is *None*, for the latest version.

        Returns:
            The intermediate data, a dictionary.

        """
        if self.database not in databases:
            raise UnknownObject("This database is not yet registered")
        if version == None and config.p.get("use_cache", False) and \
                self.database in config.cache:
            return config.cache[self.database]
        try:
            data = pickle.load(open(os.path.join(config.dir, "intermediate",
                self.filename(version)), "rb"))
            if version == None and config.p.get("use_cache", False):
                config.cache[self.database] = data
            return data
        except OSError:
            raise MissingIntermediateData("This version (%i) not found" % version)

    def versions(self):
        """Get a list of available versions of this database.

        Returns:
            List of (version, datetime created) tuples.

        """
        directory = os.path.join(config.dir, "intermediate")
        files = natural_sort(filter(
            lambda x: ".".join(x.split(".")[:-2]) == self.database,
            os.listdir(directory)))
        return sorted([(int(name.split(".")[-2]),
            datetime.datetime.fromtimestamp(os.stat(os.path.join(
            config.dir, directory, name)).st_mtime)) for name in files])

    def process(self, version=None):
        """Process intermediate data from a Python dictionary to a `NumPy <http://numpy.scipy.org/>`_ `Structured <http://docs.scipy.org/doc/numpy/reference/arrays.classes.html#record-arrays-numpy-rec>`_ `Array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_. A structured array (also called record arrays) is a heterogeneous array, where each column has a different label and data type. These structured arrays act as a standard data format for LCA and Monte Carlo calculations, and are the native data format for the Stats Arrays package.

        Processed arrays are saved in the ``processed`` directory.

        Args:
            * *version* (int, optional): The version of the database to process

        """
        data = self.load(version)
        num_exchanges = sum([len(obj["exchanges"]) for obj in data.values()])
        assert data
        dtype = [('uncertainty_type', np.uint8),
            ('input', np.uint32),
            ('output', np.uint32),
            ('row', np.uint32),
            ('col', np.uint32),
            ('technosphere', np.bool),
            ('amount', np.float32),
            ('sigma', np.float32),
            ('minimum', np.float32),
            ('maximum', np.float32),
            ('negative', np.bool)]
        arr = np.zeros((num_exchanges, ), dtype=dtype)
        arr['minimum'] = arr['maximum'] = arr['sigma'] = np.NaN
        count = 0
        for key in data:
            for exc in data[key]["exchanges"]:
                arr[count] = (
                    exc["uncertainty type"],
                    mapping[exc["input"]],
                    mapping[key],
                    MAX_INT_32,
                    MAX_INT_32,
                    exc["technosphere"],
                    exc["amount"],
                    exc.get("sigma", np.NaN),
                    exc.get("minimum", np.NaN),
                    exc.get("maximum", np.NaN),
                    exc["amount"] < 1
                    )
                count += 1

        filepath = os.path.join(config.dir, "processed", "%s.pickle" % \
            self.database)
        with open(filepath, "wb") as f:
            pickle.dump(arr, f, protocol=pickle.HIGHEST_PROTOCOL)

    def __unicode__(self):
        return u"Brightway2 database %s" % self.database

    def __str__(self):
        return self.__unicode__()
