from serialization import SerializedDict, PickledDict


class Mapping(PickledDict):
    _filename = "mapping.pickle"

    def add(self, keys):
        index = max(self.data.values())
        for i, key in enumerate(keys):
            if key not in self.data:
                self.data[key] = index + i + 1
        self.flush()

    def delete(self, keys):
        for key in keys:
            del self.data[key]
        self.flush()

    def __setitem__(self, key, value):
        raise NotImplemented

    def __unicode__(self):
        return u"Mapping from databases and methods to parameter indices."


class Databases(SerializedDict):
    _filename = "databases.json"

    def increment_version(self, database):
        self.data[database]["version"] += 1
        self.flush()
        return self.data[database]["version"]

    def version(self, database):
        return self.data[database]["version"]

    def __unicode__(self):
        return u"Brightway2 databases metadata with %i objects" % len(
            self.data)


class Methods(SerializedDict):
    _filename = "methods.json"

    def pack(self, data):
        # Transform to list because JSON can't handle lists as keys
        return [(k, v) for k, v in data.iteritems()]

    def unpack(self, data):
        # Tuples can be dict keys, but not lists; JSON can't encode tuples
        return dict([(tuple(x[0]), x[1]) for x in data])

    def __unicode__(self):
        return u"Brightway2 methods metadata with %i objects" % len(
            self.data)


mapping = Mapping()
databases = Databases()
methods = Methods()
