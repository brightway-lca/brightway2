import os
from . import config
try:
    import cPickle as pickle
except ImportError:
    import pickle


class Mapping(object):
    _filepath = os.path.join(config.dir, "mapping.pickle")

    def __init__(self):
        self.reload()

    def reload(self):
        try:
            self._data = pickle.load(open(self._filepath, "rb"))
        except IOError:
            # Create if not present
            self._data = {}
            self.flush()

    def add(self, keys):
        index = max(self._data.values())
        for i, key in enumerate(keys):
            if key not in self._data:
                self._data[key] = index + i + 1
        self.flush()

    def delete(self, keys):
        for key in keys:
            del self._data[key]
        self.flush()

    def flush(self):
        with open(self._filepath, "wb") as f:
            pickle.dump(self._data, f, protocol=pickle.HIGHEST_PROTOCOL)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        raise NotImplemented

    def __contains__(self, key):
        return key in self._data
