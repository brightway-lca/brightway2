# -*- coding: utf-8 -*
from . import databases, config, mapping
from errors import MissingIntermediateData, UnknownObject
import os
import numpy as np
from query import Query
from utils import natural_sort, MAX_INT_32
from validate import db_validator
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Database(object):
    """A manager for a database. This class can register or deregister databases, write intermediate data, process data to parameter arrays, query, validate, and copy databases.

    Databases are automatically versioned.

    The Database class never holds intermediate data, but it can load or write intermediate data. The only attribute is *database*, which is the name of the database being managed."""
    def __init__(self, database):
        """Instantiate a Database object.

        Does not load any data. If this database is not yet registered in the metadata store, a warning is written to **stdout**.

        Args:
            *database* (str): Name of the database to manage.

        """
        self.database = database
        if self.database not in databases:
            print "Warning: %s not a currently installed database" % database

    def query(self, *queries):
        """Search through the database. See :class:`query.Query` for details."""
        return Query(*queries)(self.load())

    def copy(self, name):
        """Make a copy of the database.

        Args:
            *name* (str): Name of the new database.

        """
        # Todo: register copied method
        raise NotImplemented
        assert name not in databases, ValueError("This database exists")
        def relabel_exchanges(obj, keys):
            for e in obj['exchanges']:
                if e["input"] in data:
                    e["input"] = (name, e["input"][1])
            return obj
        data = self.load()
        data = dict([((name, k[1]), relabel_exchanges(v)) for k, v in data.iteritems()])
        self.write(data, name)

    def register(self, format, depends, num_processes):
        """Register a database with the metadata store.

        Databases must be registered before data can be written.

        Args:
            *format* (str): Format that the database was converted from, e.g. "Ecospold"
            *depends* (list): Names of the databases that this database references, e.g. "biosphere"
            num_processes (int): Number of processes in this database.

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
        """Validate data (that is presumably not yet written).

        Args:
            *data* (dict): The data, in its processed form.

        """
        db_validator(data)
        return True

    def write(self, data, name=None):
        """"""
        if self.database not in databases:
            raise UnknownObject("This database is not yet registered")
        databases.increment_version(self.database)
        mapping.add(data.keys())
        filename = "%s.%i.pickle" % (self.database,
            databases.version(self.database))
        filepath = os.path.join(config.dir, "intermediate", filename)
        with open(filepath, "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self, version=None):
        """Load the intermediate data for this database.

        Can also load previous versions of this database's intermediate data.

        Args:
            *version* (int): Version of the database to load. Default is *None*, for the latest version.

        Returns:
            The intermediate data, a dictionary.

        """
        if self.database not in databases:
            raise UnknownObject("This database is not yet registered")
        files = filter(lambda x: ".".join(x.split(".")[:-2]) == self.database,
            os.listdir(os.path.join(config.dir, "intermediate")))
        if not files:
            raise MissingIntermediateData("Can't load intermediate data")
        if version == None:
            return pickle.load(open(os.path.join(config.dir, "intermediate",
                natural_sort(files)[-1]), "rb"))
        else:
            filepath = os.path.join(config.dir, "intermediate",
                "%s.%i.pickle" % (self.database, version))
            if not os.path.exists(filepath):
                raise MissingIntermediateData("This version not found")
            return pickle.load(open(filepath, "rb"))

    def process(self, version=None):
        """Create numpy structured arrays from database"""
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
