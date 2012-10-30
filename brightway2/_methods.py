# -*- coding: utf-8 -*
import os
import numpy as np
from . import config, mapping
from utils import MAX_INT_32
try:
    import cPickle as pickle
except:
    import pickle


class Methods(object):
    _filepath = os.path.join(config.dir, "methods.pickle")

    def __init__(self):
        self.reload()

    def reload(self):
        try:
            self._data = pickle.load(open(self._filepath, "r"))
        except IOError:
            # Create if not present
            self._data = {}
            self.flush()

    def add(self, name, data):
        self._data[name] = data
        self.flush()

    def delete(self, name):
        del self._data[name]
        self.flush()

    def flush(self):
        with open(self._filepath, "wb") as f:
            pickle.dump(self._data, f, protocol=pickle.HIGHEST_PROTOCOL)

    @property
    def list(self):
        return self._data.keys()

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, key):
        return key in self._data

    def process(self, name):
        """Create numpy structured arrays for IA method"""
        data_filepath = os.path.join(config.dir, "ia", "%s.pickle" % self[
            name]["abbreviation"])
        data = pickle.load(open(data_filepath, "rb"))
        assert data
        num_cfs = len(data)
        dtype = [('uncertainty_type', np.uint8),
            ('flow', np.uint32),
            ('index', np.uint32),
            ('amount', np.float32),
            ('sigma', np.float32),
            ('minimum', np.float32),
            ('maximum', np.float32),
            ('negative', np.bool)]
        arr = np.zeros((num_cfs, ), dtype=dtype)
        arr['minimum'] = arr['maximum'] = arr['sigma'] = np.NaN
        for i, cf in enumerate(data):
            arr[i] = (
                0,
                mapping[cf[0]],
                MAX_INT_32,
                cf[1],
                np.NaN,
                np.NaN,
                np.NaN,
                False
                )
        filepath = os.path.join(config.dir, "processed", "%s.pickle" % \
            self[name]["abbreviation"])
        with open(filepath, "wb") as f:
            pickle.dump(arr, f, protocol=pickle.HIGHEST_PROTOCOL)
