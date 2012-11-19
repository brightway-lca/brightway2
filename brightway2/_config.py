# -*- coding: utf-8 -*-
import os
import json
import tempfile


class Config(object):
    """A singleton that store configuration settings. Default data directory is ``brightway`` in the user's home directory, and is stored as ``config.dir``. Other configuration settings can also be assigned as needed.

    Args:
        *path* (str, optional): The path of the data directory. Must be writeable.

    """
    version = 0.1
    basic_directories = ("processed", "intermediate", "backups", "logs")

    def __init__(self, path=None):
        self.is_temp_dir = False
        self.reset(path)

    def check_dir(self, dir=None):
        """Check is directory is writeable."""
        return os.access(dir or self.dir, os.W_OK)

    def reset(self, path=None):
        """Reset to original configuration. Useful for testing."""
        # Use _dir instead of dir beacuse need to check dir ourselves
        self._dir = self.get_home_directory(path)
        if not self.check_dir():
            self.dir = tempfile.mkdtemp()
            self.is_temp_dir = True
            print "Your changes will not be saved! Set a writeable directory!"
            print "Current data directory is:"
            print self.dir
        self.load_preferences()

    def load_preferences(self):
        """Load a set of preferences from a file in the home directory.

        Preferences as stored as ``config.p``."""
        try:
            self.p = json.load(open(os.path.join(
                self.dir, "preferences.json")))
        except:
            self.p = {}

    def save_preferences(self):
        """Serialize preferences to disk."""
        with open(os.path.join(self.dir, "preferences.json"), "w") as f:
            json.dump(self.p, f, indent=2)

    def get_home_directory(self, path=None):
        """Get data directory, trying in order:

        * Provided path (optional)
        * ``BRIGHTWAY2-DIR`` environment variable
        * ``brightway2`` in user's home directory

        To set the environment variable:

        * Unix/Max: ``export BRIGHTWAY2_DIR=/path/to/brightway2/directory``
        * Windows: ``set BRIGHTWAY2_DIR=\path\to\brightway2\directory``

        """
        if path:
            return path
        envvar = os.getenv("BRIGHTWAY2_DIR")
        if envvar:
            return envvar
        else:
            return os.path.expanduser("~/brightway2")

    def request_dir(self, dirname):
        """Return ``True`` if directory already exists or can be created."""
        path = os.path.join(self.dir, dirname)
        if self.check_dir(path):
            return path
        else:
            try:
                os.mkdir(path)
                return path
            except:
                return False

    def create_basic_directories(self):
        """Create basic directory structure.

        Useful when first starting or for tests."""
        for name in self.basic_directories:
            os.mkdir(os.path.join(self.dir, name))

    def _get_dir(self):
        return self._dir

    def _set_dir(self, d):
        self._dir = d
        if not self.check_dir():
            raise OSError("This directory is not writeable")

    dir = property(_get_dir, _set_dir)


config = Config()
