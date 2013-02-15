Tutorials
*********

Getting started
===============

<insert online tutorial here>

The command line interface
==========================

The following commands are available:

    * ``bw2-controller.py list databases``: List all installed databases
    * ``bw2-controller.py list methods``: List all installed methods
    * ``bw2-controller.py details <name>``: Give details on inventory database ``<name>``. If the database name has spaces in it, it should be quoted, like this: ``"name with spaces"``.
    * ``bw2-controller.py copy <name> <newname>``: Copy inventory database ``<name>`` to new name ``<newname>``.
    * ``bw2-controller.py backup <name>``: Make a backup copy of inventory database ``<name>``.
    * ``bw2-controller.py validate <name>``: Validate the data in inventory database ``<name>``.
    * ``bw2-controller.py versions <name>``: List the versions available of inventory database ``<name>``.
    * ``bw2-controller.py revert <name> <revision>``: Revert inventory database ``<name>`` to version number ``<revision>``.
    * ``bw2-controller.py remove <name>``: Deregister inventory database ``<name>``. Does not delete data, only removes it from the Brightway2 register.
    * ``bw2-controller.py import <path> <name>``: Import a set of inventory data in the Ecospold data format from location ``<path>`` to inventory database ``<name>``.
    * ``bw2-controller.py export <name> [--include-dependencies]``: Export inventory database ``<name>`` to a bw2package format. If ``--include-dependencies`` is part of the command, the bw2package will include the dependent databases as well.
    * ``bw2-controller.py setup``: Do the initial setup for when Brightway2 is first installed.

Other online examples
=====================

<insert link to examples page here>
