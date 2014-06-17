.. _data-directory:

Data directory
**************

All Brightway2 data is stored in a single directory, the location of which is chosen by the user. The data directory has some metadata files, and a bunch of subdirectories for storing different kinds of data. Because it is a single directory, it is safe for backup programs or sync services like Dropbox.

A separate data directory can be created for each project. However, each data directory is self-contained, so each must contain a copy of e.g. ecoinvent.

Data directory structure
========================

::

    files:
        geomapping.pickle - Listing of all locations in all databases and methods
        mapping.pickle ---- Listing of all activities and flows in all LCI databases
        databases.json ---- Metadata about LCI databases
        methods.json ------ Metadata about LCIA methods
        normalizations.json Metadata about LCIA normalizations
        weightings.json --- Metadata about LCIA weightings
        preferences.json -- User settings
    subdirectories:
        backups ----------- LCI database backups
        downloads --------- Location where downloaded data is stored
        export ------------ For exported data
        intermediate ------ Storage of LCI databases and LCIA method documents
        logs -------------- Logs of Brightway2 activity
        output ------------ Calculation of data manipulation outputs written to files
        processed --------- Compressed numerical arrays made from LCI and LCIA documents
        reports ----------- Data from LCA calculations

New subdirectories can be created using `bw2data.config.request_dir <http://bw2data.readthedocs.org/en/latest/configuration.html#bw2data._config.Config.request_dir>`_.

Data directory is controlled by the ``config`` object
=====================================================

The data directory location, as well as all other configuration options and user preferences, is controlled by a singleton object call ``config``, which is created when Brightway2 is first imported. The `config <http://bw2data.readthedocs.org/en/latest/configuration.html>`_ object has its own technical reference.

Data directory location
-----------------------

.. note::
    You can ignore all these technical details if you create a file called ``brightway2`` in your home directory, and don't want to do anything fancy.

The user can specify the ``data directory`` location in three different ways. In all cases, the directory should already exist, and should be empty. The first thing that Brightway will look for is the `environment variable <http://foo.bar>`_ ``BRIGHTWAY2_DIR``. If this is found, then it is the location of the ``data directory``. An environment variable is especially convenient if you have multiple copies of Brightway2 installed on one machine, or if you want to keep separate workspaces for different projects.

To set an environment variable:

    * Unix/Mac: ``export BRIGHTWAY2_DIR=/path/to/brightway2/directory``. Add this to your ``.profile`` or similar file to have this set each time you open a terminal window.
    * Windows 7/8: Use ``setx BRIGHTWAY2_DIR=\path\to\brightway2\directory`` to set an environment variable permanently. Power users should consider SeetEnv <http://www.codeproject.com/Articles/12153/SetEnv>`_.

The second thing that Brightway2 will try is a file called ``.brightway2path`` in your home directory. If this file is present, it should have one line, which is the directory location. No quoting or special characters are needed.

Because it can be difficult to work with so-called "dot-files", whose name starts with a ``.``, Brightway2 will also try to read a file call ``brightway2path.txt`` in your home directory. This works the same as the ``.brightway2path`` file.

Finally, Brightway2 will try to see if there is a writeable directory in your home directory called ``brightway2``.

If none of these attempts succeed, Brightway2 will create and user a temporary directory, but will complain about it, as these directories can be deleted by the operating system.
