# -*- coding: utf-8 -*
import os
import tempfile


class Config(object):
    def __init__(self, path=None):
        self.reset(path)

    def check_dir(self):
        pass

    def reset(self, path=None):
        """Reset to original configuration. Useful for testing."""
        self.dir = self.get_home_directory(path)
        if not os.access(self.dir, os.W_OK):
            print "Using temporary directory:"
            self.dir = tempfile.mkdtemp()
            print self.dir
            print "Your changes will not be saved! Set a writeable directory!"
        self.check_dir()

    def get_home_directory(self, path):
        if path:
            return path
        # Unix/Max: export BRIGHTWAY2-VAR=/brightway2/directory
        # Windows: set BRIGHTWAY2-VAR=\brightway2\directory
        envvar = os.getenv("BRIGHTWAY2-VAR")
        if envvar:
            return envvar
        else:
            return os.path.expanduser("~/brightway2")

    def _get_dir(self):
        return self._dir

    def _set_dir(self, d):
        self._dir = d
        self.check_dir()

    dir = property(_get_dir, _set_dir)


config = Config()
