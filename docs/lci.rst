LCI Databases
=============

A database is an organizing unit
--------------------------------

In Brightway2, a ``database`` is the term used to organize a set of activity datasets. Databases can be big, like ecoinvent, or as small as one dataset. You can have as many databases as you like, and databases can have links into other databases. You can also have two databases that each depend on each other.

Database is a subclass of DataStore
-----------------------------------

Much of the functionality of Database objects is provided by its parent class, :ref:`datastore`. The normal methods provided by a data store are:

 * **write(data)**: Write data to disk
 * **load**: Load data from disk
 * **register**: Register object with metadata store
 * **deregister**: Remove object from metadata store
 * **copy(name)**: Create a new object with name ``name``
 * **backup**: Write backup of data
 * **validate(data)**: Validate data using this object's validator

Data store objects are instantiated with the object name, e.g. ``DataStore("name goes here")``.

Brightway2-data defines the following data stores:

    * :ref:`database`
    * :ref:`method`
    * :ref:`weighting`
    * :ref:`normalization`

.. _database-documents:

LCI datasets are documents
--------------------------

A database consists of inventory datasets, and inventory datasets are text documents, human-readable data that you can manipulate manually in a text editor, or change en masse programmatically. Because they can be exported as text, and in a format that is accessible to almost every computer language (`JSON <http://www.json.org/>`_), activity datasets can be easily exported and used by other programs.

Inventory datasets have a very flexible and free text form; even an empty dictionary (e.g. ``{}``) is a valid LCI dataset in Brightway2. However, some fields are suggested for common use. Note that you can always add extra fields as needed by your application. Here is a selection from an example dataset from the US LCI:

.. code-block:: python

    {
     'categories': ['Wood Product Manufacturing', 'Softwood Veneer and Plywood Mnf.'],
     'location': 'RNA',
     'name': 'Green veneer, at plywood plant, US PNW',
     'type': 'process',
     'unit': 'kilogram'}
     'exchanges': [{
       'amount': 1.0,
       'code': 6,
       'group': 2,
       'input': ('US LCI', '6ddb4cc00f9e42aa48515248256c31dc'),
       'type': 'production',
       'uncertainty type': 0},
      {'amount': 7.349999999999999e-06,
       'code': 5,
       'group': 4,
       'input': ('biosphere', '51447e58e03a40a2bbd9abf45214b7d3'),
       'type': 'biosphere',
       'uncertainty type': 0}],
    }

The document structure is:

* *name* (string): Name of this activity.
* *type* (string): If this is ``"process"``, or omitted completely, Brightway2 will treat this as a inventory process with inputs and output(s). If you want to store additional information in a Database outside of the list of processes, specify a custom type here. For example, the list of biosphere flows is also an inventory database, but as these are flows, not processes, they have the type ``"emission"``. Similarly, if you wanted to separate processes and products, you could create database entries for the products, with the type ``"product"``.
* *categories* (list of strings, optional): A list of categories and subcategories. Can have any length.
* *location* (string, optional): A location identifier. Default is *GLO*, but this can be changed in the :ref:`user-preferences`.
* *unit* (string): Unit of this activity. Units are normalized when written to disk.
* *exchanges* (list): A list of activity inputs and outputs, with its own schema.
    * *input* (database name, database code): The technological activity that is linked to, e.g. ``("my new database", "production of ice cream")`` or ``('biosphere', '51447e58e03a40a2bbd9abf45214b7d3')``. See also :ref:`dataset-codes`.
    * *type* (string): One of ``production``, ``technosphere``, and ``biosphere``.
        * ``production`` is an exchange that describes how much this activity produces. A ``production`` exchange is not required - the default value is 1.
        * ``technosphere`` is an input of a technosphere flow from another activity dataset.
        * ``biosphere`` is a resource consumption or emission to the environment.
    * *amount* (float): Amount of this exchange.
    * *uncertainty type* (integer): Integer code for uncertainty distribution of this exchange, see :ref:`uncertainty-type` for more information. There can be other uncertainty fields as well.
    * *comment* (string, optional): A comment on this exchange. Used to store pedigree matrix data in ecoinvent v2.

The schema for an ``LCI dataset`` in `voluptuous <https://pypi.python.org/pypi/voluptuous/>`_ is:

.. code-block:: python

    {
        Optional("categories"): Any(list, tuple),
        Optional("location"): object,
        Optional("unit"): basestring,
        Optional("name"): basestring,
        Optional("type"): basestring,
        Optional("exchanges"): [exchange]
    }

Where an ``exchange`` is:

.. code-block:: python

    {
        Required("input"): valid_tuple,
        Required("type"): basestring,
        Required("amount"): Any(float, int),
        Optional("uncertainty type"): int,
        Optional("loc"): Any(float, int),
        Optional("scale"): Any(float, int),
        Optional("shape"): Any(float, int),
        Optional("minimum"): Any(float, int),
        Optional("maximum"): Any(float, int)
    }

.. note::
    Database documents can be validated with ``bw2data.validate.db_validator(my_data)``, or ``Database("my database name").validate(my_data)``.

Databases can be stored in different ways
-----------------------------------------

The default storage backend for databases stores each database in a separate file. This is the easiest and most convenient approach for most cases. However, Brightway2 also supports pluggable database backends, which can change how databases are stored and queried.

Brightway2-data also provides ``bw2data.backends.JSONDatabase``, which stores each dataset as a separate file serialized to JSON. This approach works well with version-control systems, as each change can be saved individually. Use of ``JSONDatabase`` is shown in a simple `ipython notebook <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/JSON%20database.ipynb>`_.

Before using ``JSONDatabase``, please read its technical documentation carefully: :ref:`json-database`. To create a ``JSONDatabase``, use ``Database("my db name", backend="json")``.

:ref:`custom-backends`, such as using an actual relational database, can also be defined.

Database metadata
-----------------

No metadata is required for ``Database``s; Brightway2 will automatically set ``depends`` to a list of each linked database. The default single-file database backend will also add a ``version`` number, which is used in versioning the database.

Therefore, for ``Database`` you can simply do: ``my_database.register()``.

.. _exchanges:

Exchanges
---------

Exchanges are a list of the inputs and outputs of an activity. For example an activity might consume some resources, emit some emissions, and have other technoligcal goods as emissions. Each activity also has at least one technological output.

Each exchange has a ``type``. There are three standard exchange types in Brightway2, but you can define your own if you need to define different kinds of systems.

Production exchanges
~~~~~~~~~~~~~~~~~~~~

A production exchange defines how much of the output is produced by an activity. For example, the process "make a fizzbang" would produce one kilogram of fizzbang (the amount is normally one, but doesn't have to be).

Production exchanges have the type ``production``.

.. note:: A production exchange is **not** required. A default value of one will be applied if no production exchange is defined. This default value is usually the most logical amount, so should only be changed in special circumstances.

.. warning:: Using a production value other than one can be confusing. See the blog post `What happens with a non-unitary production amount in LCA? <http://chris.mutel.org/non-unitary.html>`_.

.. warning:: Multioutput processes (i.e. more than one production process) can be used in Brightway2, but only under special circumstances. See the blog post `Multi-output processes in matrix-based LCA <http://example.com>`_.

Technosphere exchanges
~~~~~~~~~~~~~~~~~~~~~~

A technosphere exchange is an process input from the technosphere, i.e. the industrial economy. For example, the process "make a fizzbang" could have an input of seven kilograms of lollies.

Technosphere exchanges have the type ``technosphere``.

Biosphere exchanges
~~~~~~~~~~~~~~~~~~~

A biosphere exchange is a consumption of a resource or and emission to the environment associated with a process; its value will be placed in the biosphere matrix.

Biosphere exchanges have the type ``biosphere``.

.. _biosphere-database:

Biosphere database
------------------

Starting Brightway2 through the web interface, or when you run ``bw2setup()`` in a python shell, Brightway2 downloads and installs a special ``biosphere`` database. This database has all the resource and emission flows from the ecoinvent database, version 2.

You can define biosphere flows - resources and emissions - in any database you like, but it is probably best to use the pre-defined flows in the ``biosphere`` database whenever you can. If you need to add some custom flows, feel free to create a separate new database.

You can also change the name for the default biosphere database in the :ref:`user preferences <user-preferences>`.

.. _dataset-codes:

Uniquely identifying datasets
-----------------------------

Linking activity datasets within and between databases requires a way to uniquely identify each dataset - Brightway2 calls this unique identifier a code. A code can be a number, like ``1``, or a string of numbers and letters, like ``swiss ch33se``. When you create datasets manually, you will need to assign each dataset a code. When you import a database, the codes will be automatically generated for you.

Activity hashes
~~~~~~~~~~~~~~~

When you import an *ecospold* or *SimaPro* dataset, the data format does not provide a . Brightway2 will generate codes that look like a bunch of nonsense, e.g.: ``6d336c64e3a0ff08dee166a1dfdf0946``. In this case, Brightway2 identifies an activity or flow with the `MD5 <http://en.wikipedia.org/wiki/MD5>`_ hash of a few attributes: For ecoinvent 2, the ``name``, ``location``, ``unit``, and ``categories``. For ecoinvent 3, the ``activity`` and ``reference product`` names. The function that computes the activity hash is :ref:`bw2data.utils.activity_hash <activity-hash>`.

Searching databases
-------------------

Brightway2 includes some simple functions for searching within databases. Because a database is a simple Python dictionary, it is relatively simple to filter and process. In other words, searching in Brightway2 is at a very low level - you can do a lot, but it might be a bit harder than it should be.

The basic strategy is to start with an entire database, i.e. a set of datasets, and progressively apply filters until a smaller set of datasets is left over. In python code, it would be something like this:

.. code-block:: python

    database = [{'name': 'foo'}, {'name': 'bar'}]
    def search_filter(datasets, string):
        return [
                obj for obj in datasets
                if string in obj.get('name')
        ]
    results = search_filter(database)

Filters can be inclusive or exclusive. Brightway2 provides a generic :ref:`search-filter` class that can filter based on a specific data attribute, but you can also create filters that consider any aspect of a dataset that you like.

One or more ``Filter`` s get applied with the help of a :ref:`search-query` object, which just prepares the filter to be applied to a database.

The output from a applying a ``Query`` to a set of datasets is a search :ref:`search-result`. A ``Result`` is like a database object, in that it is a dictionary with dataset documents, but is read-only and only has a ``.sort()`` method, which sorts that dictionary by a field value in ascending or descending order.

See the linked technical documentation, and a `notebook on database searching <http://example.com>`_.



.. code-block:: python

    In [1]: from bw2data.query import *
    In [2]: from bw2data import *
    In [3]: ei = Database("ecoinvent 2.2")
    In [4]: r = ei.query(Filter("name", "in", "at long-distance pipeline"))
    In [5]: len(r)
    Out[5]: 8

    In [6]: print r
    Query result with 8 entries

    In [7]: r
    Out[7]:
    Query result: (total 8)
    ('ecoinvent 2.2', 1427): natural gas, production DZ, at long-distance pipeline
    ('ecoinvent 2.2', 1425): natural gas, production DE, at long-distance pipeline
    ('ecoinvent 2.2', 1413): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1412): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1432): natural gas, production RU, at long-distance pipeline
    ('ecoinvent 2.2', 1431): natural gas, production NO, at long-distance pipeline
    ('ecoinvent 2.2', 1430): natural gas, production NL, at long-distance pipeline
    ('ecoinvent 2.2', 1429): natural gas, production GB, at long-distance pipeline

    In [8]: r.sort("name")
    In [9]: r
    Out[9]:
    Query result: (total 8)
    ('ecoinvent 2.2', 1413): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1412): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1425): natural gas, production DE, at long-distance pipeline
    ('ecoinvent 2.2', 1427): natural gas, production DZ, at long-distance pipeline
    ('ecoinvent 2.2', 1429): natural gas, production GB, at long-distance pipeline
    ('ecoinvent 2.2', 1430): natural gas, production NL, at long-distance pipeline
    ('ecoinvent 2.2', 1431): natural gas, production NO, at long-distance pipeline
    ('ecoinvent 2.2', 1432): natural gas, production RU, at long-distance pipeline

    In [10]: q = Query(Filter("unit", "iis", "tkm"), Filter("name", "in", "lorry"))
    In [11]: r = q(ei.load())
    In [12]: len(r)
    Out[12]: 19

Import and Export
-----------------

Import and export of LCI databases is covered in the technical documentation: :ref:`import-and-export`.
