# -*- coding: utf-8 -*
from . import config, mapping, methods
from errors import UnknownObject, MissingIntermediateData
from utils import MAX_INT_32
import numpy as np
import os
import random
import string
from validate import ia_validator
try:
    import cPickle as pickle
except ImportError:
    import pickle


def abbreviate(names, length=8):
    abbrev = lambda x: x if x[0] in string.digits else x[0].lower()
    name = " ".join(names).split(" ")[0].lower() + \
        "".join([abbrev(x) for x in " ".join(names).split(" ")[1:]])
    random_string = ''.join(random.choice(string.letters + string.digits
        ) for i in xrange(length))
    return name + "-" + random_string


class Method(object):
    """A manager for a method. This class can register or deregister databases, write intermediate data, process data to parameter arrays, query, validate, and copy databases.

    Databases are automatically versioned.

    The Database class never holds intermediate data, but it can load or write intermediate data. The only attribute is *database*, which is the name of the database being managed."""
    def __init__(self, method, *args, **kwargs):
        self.method = method
        if self.method not in methods:
            print "Warning: %s not a currently installed method" % (
                " : ".join(method))

    def get_abbreviation(self):
        try:
            return methods[self.method]["abbreviation"]
        except KeyError:
            raise UnknownObject("This method is not yet registered")

    def copy(self, name):
        # Todo: This doesn't work yet
        self.write(self.load(), name)

    def register(self, unit, description="", num_cfs=0):
        assert self.method not in methods
        methods[self.method] = {
            "abbreviation": abbreviate(self.method),
            "unit": unit,
            "description": description,
            "num_cfs": num_cfs
            }

    def deregister(self):
        del methods[self.method]

    def validate(self, data):
        ia_validator(data)
        return True

    def write(self, data):
        if self.method not in methods:
            raise UnknownObject("This database is not yet registered")
        mapping.add(data.keys())
        filepath = os.path.join(config.dir, "intermediate",
            "%s.pickle" % self.get_abbreviation())
        with open(filepath, "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        try:
            return pickle.load(open(os.path.join(config.dir, "intermediate",
                "%s.pickle" % self.get_abbreviation()), "rb"))
        except OSError:
            raise MissingIntermediateData("Can't load intermediate data")

    def process(self):
        """Create numpy structured arrays for IA method"""
        data = pickle.load(open(os.path.join(config.dir, "intermediate",
            "%s.pickle" % self.get_abbreviation()), "rb"))
        assert data
        dtype = [('uncertainty_type', np.uint8),
            ('flow', np.uint32),
            ('index', np.uint32),
            ('amount', np.float32),
            ('sigma', np.float32),
            ('minimum', np.float32),
            ('maximum', np.float32),
            ('negative', np.bool)]
        arr = np.zeros((len(data), ), dtype=dtype)
        arr['minimum'] = arr['maximum'] = arr['sigma'] = np.NaN
        for i, (key, value) in enumerate(data.iteritems()):
            arr[i] = (
                0,
                mapping[key],
                MAX_INT_32,
                value,
                np.NaN,
                np.NaN,
                np.NaN,
                False
                )
        filepath = os.path.join(config.dir, "processed", "%s.pickle" % \
            self.get_abbreviation())
        with open(filepath, "wb") as f:
            pickle.dump(arr, f, protocol=pickle.HIGHEST_PROTOCOL)
