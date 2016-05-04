Brightway2-data
***************

.. _configuration-technical:

Configuration
=============

The configuration for brightway2 is implemented as a singleton class that is created when ``brightway2`` is imported.

.. autoclass:: bw2data.configuration.Config
    :members:

Projects
========

.. autoclass:: bw2data.project.ProjectManager
    :members:

Base classes for metadata
=========================

.. _serialized-dict:

Serialized Dictionary
---------------------

.. autoclass:: bw2data.serialization.SerializedDict
    :members:

.. _compound-json:

Compound JSON dictionary
------------------------

JSON hash tables don't support keys like ``("biosphere", "an emission")``, so the ``pack`` and ``unpack`` methods are used to transform data from Python to JSON and back.

.. autoclass:: bw2data.serialization.CompoundJSONDict
    :members:

.. _pickled-dict:

Pickled Dictionary
------------------

.. autoclass:: bw2data.serialization.PickledDict
    :members:

Metadata stores
===============

.. _databases:

databases
---------

.. autoclass:: bw2data.meta.Databases
    :members:
    :inherited-members:

.. _methods:

methods
-------

.. autoclass:: bw2data.meta.Methods
    :members:
    :inherited-members:

.. _normalizations:

normalizations
--------------

.. autoclass:: bw2data.meta.NormalizationMeta
    :members:

.. _weightings:

weightings
----------

.. autoclass:: bw2data.meta.WeightingMeta
    :members:

Mappings
========

.. _mapping:

mapping
-------

.. autoclass:: bw2data.meta.Mapping
    :members:

.. _geomapping:

geomapping
----------

.. autoclass:: bw2data.meta.GeoMapping
    :members:

Data stores
===========

.. _datastore:

DataStore
---------

.. autoclass:: bw2data.DataStore
    :members:

Inventory data backends
=======================

.. _database:

DatabaseChooser
---------------

The function :func:`bw2data.database.DatabaseChooser` will choose the correct ``Database`` class depending on the database backend registered for the database in its metadata. ``bw2data`` comes with two backends (see :ref:`database-backends`).

The function ``bw2data.database.Database`` is an alias for :func:`bw2data.database.DatabaseChooser`, provided for backwards compatibility.

.. autofunction:: bw2data.database.DatabaseChooser

.. _switching-backends:

Switching backends
------------------

.. autofunction:: bw2data.backends.utils.convert_backend

.. _custom-backends:

Custom database backends
------------------------

New database backends should inherit from ``bw2data.backends.base.LCIBackend``:

.. autoclass:: bw2data.backends.base.LCIBackend
    :members:

.. _single-file-database:

Default backend - databases stored in a SQLite database
-------------------------------------------------------

This backend is a hybrid between SQLite and a document database. See also :ref:`whysqlite`

The LCI data is stored in two tables, `ActivityDataset` and `ExchangeDataset`. Interactions with the database are mostly done using the `Peewee ORM <http://docs.peewee-orm.com/en/latest/>`__, although some raw SQL queries are used for performance reasons. The table have the following schemas:

.. code:: sql

    CREATE TABLE "activitydataset" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "data" BLOB NOT NULL,
        "code" TEXT NOT NULL,
        "database" TEXT NOT NULL,
        "location" TEXT,
        "name" TEXT,
        "product" TEXT,
        "type" TEXT
    )

    CREATE TABLE "exchangedataset" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "data" BLOB NOT NULL,
        "input_code" TEXT NOT NULL,
        "input_database" TEXT NOT NULL,
        "output_code" TEXT NOT NULL,
        "output_database" TEXT NOT NULL,
        "type" TEXT NOT NULL
    )

As one of the fundamental principles of Brightway2 is to have a document-based backend, we incude most data in the column `data`, which is stored as a binary pickle. Serializing and deserializing is handled automatically by the Peewee interface. However, some attributes can be changed in the database. The following columns are canonical, i.e. they are included when constructing the `Activity` and `Exchange` objects:

* ActivityDataset.database
* ActivityDataset.code
* ExchangeDataset.input_database
* ExchangeDataset.input_code
* ExchangeDataset.output_database
* ExchangeDataset.output_code

All other columns are only used to querying and filtering datasets.

.. autoclass:: bw2data.backends.peewee.database.SQLiteBackend
    :members:

Single file - each database in a single file
--------------------------------------------

.. autoclass:: bw2data.backends.single_file.database.SingleFileDatabase
    :members:

.. _json-database:

Version-control friendly - each database is a JSON file
-------------------------------------------------------

.. autoclass:: bw2data.backends.json.database.JSONDatabase
    :members:

.. autoclass:: bw2data.backends.json.sync_json_dict.SynchronousJSONDict
    :members:

.. autoclass:: bw2data.backends.json.sync_json_dict.frozendict
    :members:

Impact Assessment data stores
=============================

.. _ia-datastore:

ImpactAssessmentDataStore
-------------------------

.. autofunction:: bw2data.ia_data_store.abbreviate

.. autoclass:: bw2data.ia_data_store.ImpactAssessmentDataStore
    :members:

.. _method:

Method
------

.. autoclass:: bw2data.method.Method
    :members:

.. _normalization:

Normalization
-------------

.. autoclass:: bw2data.weighting_normalization.Normalization
    :members:

.. _weighting:

Weighting
---------

.. autoclass:: bw2data.weighting_normalization.Weighting
    :members:

.. _user-preferences:

User preferences
================

.. autoclass:: bw2data.meta.Preferences
    :members:

Utilities
=========

.. automethod:: bw2data.utils.combine_methods

.. automethod:: bw2data.utils.download_file

.. automethod:: bw2data.utils.natural_sort

.. automethod:: bw2data.utils.random_string

.. automethod:: bw2data.utils.recursive_str_to_unicode

.. automethod:: bw2data.utils.uncertainify

