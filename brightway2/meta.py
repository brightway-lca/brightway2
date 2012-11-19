from serialization import SerializedDict, PickledDict


class Mapping(PickledDict):
    """A dictionary that maps object ids, like ``("Ecoinvent 2.2", 42)``, to integers. Needed because parameter arrays have integer ``row`` and ``column`` fields.

    File data is saved in ``mapping.pickle``.

    This dictionary does not support setting items directly; instead, use the ``add`` method to add multiple keys."""
    _filename = "mapping.pickle"

    def add(self, keys):
        """Add a set of keys. These keys can already be in the mapping; only new keys will be added.

        Args:
            *keys* (list): The keys to add.

        """
        index = max(self.data.values())
        for i, key in enumerate(keys):
            if key not in self.data:
                self.data[key] = index + i + 1
        self.flush()

    def delete(self, keys):
        """Delete a set of keys.

        Args:
            *keys* (list): The keys to delete.

        """
        for key in keys:
            del self.data[key]
        self.flush()

    def __setitem__(self, key, value):
        raise NotImplemented

    def __unicode__(self):
        return u"Mapping from databases and methods to parameter indices."

    def __len__(self):
        return len(self.data)


class Databases(SerializedDict):
    """A dictionary for database metadata. This class includes methods to manage database versions. File data is saved in ``databases.json``."""
    _filename = "databases.json"

    def increment_version(self, database):
        """Increment the ``database`` version. Returns the new version."""
        self.data[database]["version"] += 1
        self.flush()
        return self.data[database]["version"]

    def version(self, database):
        """Return the ``database`` version"""
        return self.data[database]["version"]

    def __unicode__(self):
        return u"Brightway2 databases metadata with %i objects" % len(
            self.data)


class Methods(SerializedDict):
    """A dictionary for method metadata. File data is saved in ``methods.json``."""
    _filename = "methods.json"

    def pack(self, data):
        """Transform the dictionary to a list because JSON can't handle lists as keys"""
        return [(k, v) for k, v in data.iteritems()]

    def unpack(self, data):
        """Transform data back to a dictionary"""
        return dict([(tuple(x[0]), x[1]) for x in data])

    def __unicode__(self):
        return u"Brightway2 methods metadata with %i objects" % len(
            self.data)


mapping = Mapping()
databases = Databases()
methods = Methods()


def reset_meta():
    mapping.__init__()
    databases.__init__()
    methods.__init__()
