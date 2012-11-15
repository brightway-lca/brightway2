# -*- coding: utf-8 -*
import os
import tempfile


class Config(object):
    """A singleton that store configuration settings. Default data directory is ``brightway`` in the user's home directory, and is stored as ``config.dir``. Other configuration settings can also be assigned as needed.

    Args:
        *path* (str, optional): The path of the data directory. Must be writeable.

    """
    def __init__(self, path=None):
        self.is_temp_dir = False
        self.reset(path)

    def check_dir(self, dir=None):
        """Check is directory is writeable."""
        return os.access(dir or self.dir, os.W_OK)

    def reset(self, path=None):
        """Reset to original configuration. Useful for testing."""
        self.dir = self.get_home_directory(path)
        if not self.check_dir():
            self.dir = tempfile.mkdtemp()
            self.is_temp_dir = True
            print "Your changes will not be saved! Set a writeable directory!"
            print "Current data directory is:"
            print self.dir

    def get_home_directory(self, path=None):
        """Get data directory, trying in order:

        * Provided path (optional)
        * ``BRIGHTWAY2-DIR`` environment variable
        * ``brightway2`` in user's home directory

        To set the environment variable:

        * Unix/Max: ``export BRIGHTWAY2-DIR=/path/to/brightway2/directory``
        * Windows: ``set BRIGHTWAY2-DIR=\path\to\brightway2\directory``

        """
        if path:
            return path
        envvar = os.getenv("BRIGHTWAY2-DIR")
        if envvar:
            return envvar
        else:
            return os.path.expanduser("~/brightway2")

    def request_dir(self, dirname):
        """Return ``True`` if directory already exists or can be created."""
        path = os.path.join(self.dir, dirname)
        if self.check_dir(path):
            return True
        else:
            try:
                os.mkdir(path)
                return True
            except:
                return False

    def _get_dir(self):
        return self._dir

    def _set_dir(self, d):
        self._dir = d
        if not self.check_dir():
            raise OSError("This directory is not writeable")

    dir = property(_get_dir, _set_dir)


config = Config()
