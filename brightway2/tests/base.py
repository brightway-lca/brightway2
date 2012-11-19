# -*- coding: utf-8 -*-
from .. import config
import tempfile
import unittest


class BW2Test(unittest.TestCase):
    def __setup__(self):
        config.dir = tempfile.mkdtemp()
        config.create_basic_directories()
        self.extra_setup()

    def extra_setup(self):
        pass
