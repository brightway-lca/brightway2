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
    def __init__(self, database, *args, **kwargs):
        self.database = database
        if self.database not in databases:
            print "Warning: %s not a currently installed database" % database

    def query(self, *queries):
        return Query(*queries)(self.load())

    def copy(self, name):
        # Todo: register copied method
        raise NotImplemented

        def relabel_exchanges(obj, keys):
            for e in obj['exchanges']:
                if e["input"] in data:
                    e["input"] = (name, e["input"][1])
            return obj
        data = self.load()
        data = dict([((name, k[1]), relabel_exchanges(v)) for k, v in data.iteritems()])
        self.write(data, name)

    def register(self, format, depends, num_processes):
        assert self.database not in databases
        databases[self.database] = {
            "from format": format,
            "depends": depends,
            "number": num_processes,
            "version": 0
            }

    def deregister(self):
        del databases[self.database]

    def validate(self, data):
        db_validator(data)
        return True

    def write(self, data, name=None):
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
