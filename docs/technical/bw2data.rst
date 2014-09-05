Brightway2-data
***************

.. _configuration-technical:

Configuration
=============

The configuration for brightway2 is implemented as a singleton class that is created when ``brightway2`` is imported.

.. autoclass:: bw2data._config.Config
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

Default backend - each database is a single file
------------------------------------------------

.. autoclass:: bw2data.backends.default.database.SingleFileDatabase
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

.. _searching:

Searching Databases
===================

.. _search-filter:

Filter
------

.. autoclass:: bw2data.Filter
    :members:

.. _search-query:

Query
-----

.. autoclass:: bw2data.Query
    :members:

.. _search-result:

Result
------

.. autoclass:: bw2data.Result
    :members:

Dictionaries
------------

.. autoclass:: bw2data.query.Dictionaries
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

.. autoclass:: bw2data.Method
    :members:

.. _normalization:

Normalization
-------------

.. autoclass:: bw2data.Normalization
    :members:

.. _weighting:

Weighting
---------

.. autoclass:: bw2data.Weighting
    :members:

.. _import-and-export:

Import and Export
=================

BW2Package
----------

Brightway2 has its own data format for archiving data which is both efficient and compatible across operating systems and programming languages. This is the default backup format for Brightway2 :ref:`datastore` objects.

.. note:: **imports** and **exports** are supported.

.. autoclass:: bw2data.io.BW2Package
    :members:

Ecospold1
---------

Ecospold version 1 is the data format of ecoinvent versions 1 and 2, and the US LCI. It is an XML data format with reasonable defaults.

.. note:: only **imports** are supported.

.. autoclass:: bw2data.io.Ecospold1Importer
    :members:

.. autoclass:: bw2data.io.EcospoldImpactAssessmentImporter
    :members:

Ecospold2
---------

Ecospold version 2 is the data format of ecoinvent version 3.

.. note:: only **imports** are supported.

.. autoclass:: bw2data.io.Ecospold2Importer
    :members:

SimaPro
-------

Import a `SimaPro <http://www.pre-sustainability.com/simapro-lca-software>`_ text file.

.. note:: only **imports** are supported.

.. warning:: Import of projects linked to Ecoinvent version 3 are not yet supported.

.. autoclass:: bw2data.io.SimaProImporter
    :members:

Gephi
-----

`Gephi <http://gephi.org/>`_ is an open-source graph visualization and analysis program.

.. note:: only **exports** are supported.

.. autoclass:: bw2data.io.DatabaseToGEXF
    :members:

.. autoclass:: bw2data.io.DatabaseSelectionToGEXF
    :members:

.. autofunction:: bw2data.io.keyword_to_gephi_graph

Utilities
=========

Setup
-----

.. autofunction:: bw2data.utils.bw2setup

.. _set-data-dir:

Setting the data directory
--------------------------

.. autofunction:: bw2data.utils.set_data_dir

Sorting
-------

.. autofunction:: bw2data.utils.natural_sort
.. autofunction:: bw2data.utils.recursively_sort

Identifying and labeling
------------------------

.. _activity-hash:

.. autofunction:: bw2data.utils.activity_hash
.. autofunction:: bw2data.utils.database_hash
.. autofunction:: bw2data.utils.random_string
.. autofunction:: bw2data.utils.safe_filename

Working with data
-----------------

.. autofunction:: bw2data.utils.clean_exchanges
.. autofunction:: bw2data.utils.combine_methods

.. _recursive-str-to-unicode:

.. autofunction:: bw2data.utils.recursive_str_to_unicode
.. autofunction:: bw2data.utils.uncertainify

Web utilities
-------------

.. autofunction:: bw2data.utils.download_file
.. autofunction:: bw2data.utils.open_activity_in_webbrowser
.. autofunction:: bw2data.utils.web_ui_accessible
