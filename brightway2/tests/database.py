# -*- coding: utf-8 -*-
from . import BW2Test
from .. import Database, databases
from fixtures import food, biosphere


class DatabaseTest(BW2Test):
    def extra_setup(self):
        d = Database("biosphere")
        d.register("Tests", [], len(biosphere))
        d.write(biosphere)
        d = Database("food")
        d.register("Tests", ["biosphere"], len(food))
        d.write(food)

    def test_setup(self):
        self.assertEqual(len(databases), 2)

    def test_copy(self):
        pass

    def test_relabel_data(self):
        pass

    def test_revert(self):
        pass

    def test_register(self):
        pass

    def test_load(self):
        pass

    def test_versions(self):
        pass
