# -*- coding: utf-8 -*
import os
import json
from . import config


class Meta(object):
    _filepath = os.path.join(config.dir, "meta.json")

    def __init__(self):
        self.reload()

    def reload(self):
        try:
            self._data = json.load(open(self._filepath, "r"))
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
        with open(self._filepath, "w") as f:
            json.dump(self._data, f, indent=2)

    def increment_version(self, database):
        self._data[database]["version"] += 1
        self.flush()
        return self._data[database]["version"]

    @property
    def databases(self):
        return self._data

    @property
    def list(self):
        return self._data.keys()

    def version(self, database):
        return self._data[database]["version"]

    def __getitem__(self, key):
        return self._data[key]

    def __contains__(self, key):
        return key in self._data
