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
            self._data = self.deserialize()
        except IOError:
            # Create if not present
            self._data = {}
            self.flush()

    def flush(self):
        self.serialize()

    @property
    def data(self):
        return self._data

    @property
    def list(self):
        return self._data.keys()

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value
        self.flush()

    def __contains__(self, key):
        return key in self._data

    def __str__(self):
        return self.__unicode__()

    def __delitem__(self, name):
        del self._data[name]
        self.flush()

    def serialize(self, filepath=None):
        with open(filepath or self._filepath, "w") as f:
            json.dump(self.pack(self._data), f, indent=2)

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
            pickle.dump(self.pack(self._data), f,
                protocol=pickle.HIGHEST_PROTOCOL)

    def deserialize(self):
        return self.unpack(pickle.load(open(self._filepath, "rb")))
