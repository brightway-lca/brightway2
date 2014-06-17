Databases
*********

A database is an organizing unit
================================

In Brightway2, a ``database`` is the term used to organize a set of activity datasets. Databases can be big, like ecoinvent, or as small as one dataset. You can have as many databases as you like, and databases can link into other databases. You can also have two databases that each depend on each other.

Databases can be stored in different ways
=========================================

The default storage backend for databases stores each database in a separate file. This is the easiest and most convenient approach for most cases. However, Brightway2 also supports pluggable database backends, which can change how databases are stored and queried.

Brightway2-data also provides `JSONDatabase <http://bw2data.readthedocs.org/en/latest/inventory.html#version-control-friendly-each-database-is-a-json-file>`_, which stores each dataset as a separate file serialized to JSON. This approach works well with version-control systems, as each change can be saved individually.

.. warning:: Before using ``JSONDatabase``, please read `its documentation <http://bw2data.readthedocs.org/en/latest/inventory.html#version-control-friendly-each-database-is-a-json-file>`_ carefully.

`Custom backends <http://bw2data.readthedocs.org/en/latest/inventory.html#custom-database-backends>`_, such as using an actual database, can also be defined.

LCI datasets are documents
==========================

An activity dataset is a document - just some text, with a minial amount of formatting. For example, here is a Brightway2 activity dataset from the US LCI:

.. code-block:: python

  {
  'name': 'Energy, output',
  'unit': 'megajoule'
  'categories': ['biomass', 'fuels'],
  'location': 'RNA',
  'exchanges': [{
    'amount': 11968.25,
    'input': ('biosphere', '6d336c64e3a0ff08dee166a1dfdf0946'),
    'type': 'biosphere',
  }],
  }

The technical details of the data format are described later in :ref:`database-documents`. For now, here are the important points about activity datasets being documents:

    * They are a section of human-readable data that you can manipulate manually in a text editor, or change en masse programmatically.
    * Because they can be exported as text, and in a format that is accessible to almost every computer language (`JSON <http://www.json.org/>`_), activity datasets can be easily exported and used by other programs.
    * Activity datasets have a small number of required fields, but allow any additional information you would like to add, so that it is easy to add whatever additional data you need for your application.

.. _dataset-codes:

Dataset codes
=============

Linking activity datasets within and between databases requires a way to uniquely identify each dataset - Brightway2 calls this unique identifier a code. A code can be a number, like ``1``, or a string of numbers and letters, like ``swiss ch33se``. When you create datasets manually, you will need to assign each dataset a code. When you import a database, the codes will be automatically generated for you.

Activity hashes
---------------

When you import an *ecospold* or *SimaPro* dataset, the codes that are generated automatically look like a bunch of nonsense, like this: ``6d336c64e3a0ff08dee166a1dfdf0946``. The way Brightway2 identifies an activity or flow is with the `MD5 <http://en.wikipedia.org/wiki/MD5>`_ hash of a few attributes: the ``name``, ``location``, ``unit``, and ``categories``. The function that computes the activity hash is `bw2data.utils.activity_hash <http://bw2data.readthedocs.org/en/latest/utils.html#bw2data.utils.activity_hash>`_.

.. _exchanges:

Exchanges
=========

Exchanges are a list of the inputs and outputs of an activity. For example an activity might consume some resources, emit some emissions, and have other technoligcal goods as emissions. Each activity also has at least one technological output.

Each exchange has a ``type``. There are three standard exchange types in Brightway2, but you can define your own if you need to define different kinds of systems.

Production exchanges
--------------------

A production exchange defines how much of the output is produced by an activity. For example, the process "make a fizzbang" would produce one kilogram of fizzbang (the amount is normally one, but doesn't have to be).

Production exchanges have the type ``production``.

.. note:: A production exchange is **not** required. A default value of one will be applied if no production exchange is defined. This default value is usually the most logical amount, so should only be changed in special circumstances.

.. warning:: Using a production value other than one can be confusing. See the blog post `What happens with a non-unitary production amount in LCA? <http://chris.mutel.org/non-unitary.html>`_.

.. warning:: Multioutput processes (i.e. more than one production process) can be used in Brightway2, but only under special circumstances. See the blog post `Multi-output processes in matrix-based LCA <http://example.com>`_.

Technosphere exchanges
----------------------

A technosphere exchange is an process input from the technosphere, i.e. the industrial economy. For example, the process "make a fizzbang" could have an input of seven kilograms of lollies.

Technosphere exchanges have the type ``technosphere``.

Biosphere exchanges
-------------------

A biosphere exchange is a consumption of a resource or and emission to the environment associated with a process; its value will be placed in the biosphere matrix.

Biosphere exchanges have the type ``biosphere``.

.. _biosphere-database:

Biosphere database
==================

When Brightway2 is set up, it downloads and installs a special ``biosphere`` database. This database has all the resource and emission flows from the ecoinvent database, and is the database that imported life cycle impact assessment methods will link to.

You can define biosphere flows - resources and emissions - in any database you like, but it is probably best to use the pre-defined flows in the ``biosphere`` database whenever you can. If you need to add some custom flows, feel free to create a separate new database.

You can also change the name for the default biosphere database in the `user preferences <http://bw2data.readthedocs.org/en/latest/configuration.html#bw2data._config.Config.biosphere>`_.
