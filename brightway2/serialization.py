# -*- coding: utf-8 -*
import os
from . import config
from time import time
import json
try:
    import cPickle as pickle
except ImportError:
    import pickle


class SerializedDict(object):
    def __init__(self):
        self._filepath = os.path.join(config.dir, self._filename)
        self.load()

    def load(self):
        try:
            self.data = self.deserialize()
        except IOError:
            # Create if not present
            self.data = {}
            self.flush()

    def flush(self):
        self.serialize()

    @property
    def list(self):
        return sorted(self.data.keys())

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.flush()

    def __contains__(self, key):
        return key in self.data

    def __str__(self):
        return self.__unicode__()

    def __delitem__(self, name):
        del self.data[name]
        self.flush()

    def iteritems(self):
        return self.data.iteritems()

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def serialize(self, filepath=None):
        with open(filepath or self._filepath, "w") as f:
            json.dump(self.pack(self.data), f, indent=2)

    def deserialize(self):
        return self.unpack(json.load(open(self._filepath, "r")))

    def pack(self, data):
        return data

    def unpack(self, data):
        return data

    def backup(self):
        """Write a backup version of the data to backups directory"""
        filepath = os.path.join(config.dir, "backups",
            self._filename + ".%s.backup" % int(time()))
        self.serialize(filepath)


class PickledDict(SerializedDict):
    def serialize(self):
        with open(self._filepath, "wb") as f:
            pickle.dump(self.pack(self.data), f,
                protocol=pickle.HIGHEST_PROTOCOL)

    def deserialize(self):
        return self.unpack(pickle.load(open(self._filepath, "rb")))
