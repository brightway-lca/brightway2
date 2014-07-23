Data formats
************

Databases
=========

Database metadata
-----------------

There is a very basic set of metadata stored about each inventory database, stored in the file ``databases.json``. To get the metadata about a database, do something like the following:

.. code-block:: python

    from brightway2 import *
    databases["ecoinvent 2.2"]

.. note::
    See also the `databases manager documentation <http://bw2data.readthedocs.org/en/latest/technical.html#bw2data.meta.Databases>`_

The returned metadata is:

.. code-block:: python

    {'depends': ['biosphere'],
     'version': 1}

**No metadata** is required for ``Database``s; Brightway2 will automatically set ``depends`` to a list of each linked database. The default single-file database backend will also add a ``version`` number, which is used in versioning the database. The JSON backend adds no additional metadata. To set the JSON backend for a ``Database``, add the following metadata: ``"backend": "json"``, either while registering the database (``my_database.register(backend="json")``), or by modifying the metadata directly:

.. code-block:: python

    databases["my sweet database"]["backend"] = "json"
    databases.flush()

.. _database-documents:

Database documents
------------------

A database consists of inventory datasets, and inventory datasets have a very flexible and free form. Indeed, even an empty dictionary (e.g. ``{}``) is a valid LCI dataset in Brightway2. However, some fields are suggested for common use. Note that you can always add extra fields as needed by your application. Here is a selection from an example dataset from the US LCI:

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
* *location* (string, optional): A location identifier. Default is *GLO* (but this can be changed in the user preferences; see `bw2data.config <http://bw2data.readthedocs.org/en/latest/configuration.html#bw2data._config.Config.global_location>`_).
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

.. note:: See also :ref:`exchanges` for the details on different types of exchanges.

.. note::
    Database documents can be validated with ``bw2data.validate.db_validator(my_data)``, or ``Database("my database name").validate(my_data)``.

.. _uncertainty-type:

Uncertainty types and uncertainty dictionaries
----------------------------------------------

An ``uncertainty dictionary`` has one required key: ``amount``, which specifies the most representative value (expected value/median/mode/other) of the distribution. The uncertainty distribution is defined by the key ``uncertainty type``.  Depending on the distribution, some or all of the following fields can also be specified: *loc*, *scale*, *shape*, *minimum*, and *maximum*.

The schema for an ``uncertainty dictionary`` in `voluptuous <https://pypi.python.org/pypi/voluptuous/>`_ is:

.. code-block:: python

    uncertainty_dict = {
        Required("amount"): Any(float, int),
        Optional("uncertainty type"): int,
        Optional("loc"): Any(float, int),
        Optional("scale"): Any(float, int),
        Optional("shape"): Any(float, int),
        Optional("minimum"): Any(float, int),
        Optional("maximum"): Any(float, int)
    }

The integer ``uncertainty type`` fields are defined in a separate software package called `stats_arrays <https://stats-arrays.readthedocs.org/en/latest/>`_. The uncertainty types are given below, and their parameters are explained in detail in the `stats_arrays table <https://stats-arrays.readthedocs.org/en/latest/#mapping-parameter-array-columns-to-uncertainty-distributions>`_:

    * ``0``: Undefined or unknown uncertainty.
    * ``1``: No uncertainty.
    * ``2``: Lognormal distribution. This is **purposely** handled in an inconsistent fashion, unfortunately. The ``amount`` field is the median of the data, and the ``sigma`` field is the standard deviation of the data **when it is log-transformed**, i.e. the σ from the formula for the log-normal PDF.
    * ``3``: Normal distribution.
    * ``4``: Uniform distribution.
    * ``5``: Triangular distribution.
    * ``6``: Bernoulli distribution.
    * ``7``: Discrete uniform.
    * ``8``: Weibull.
    * ``9``: Gamma.
    * ``10``: Beta distribution.
    * ``11``: Generalized Extreme Value.
    * ``12``: Student's T.

.. note:: The default value for ``uncertainty type`` is ``0``, i.e. no uncertainty.

.. note::
    All distributions (where it is applicable) can be bounded, i.e. you can specify a minimum and maximum value in addition to other parameters. This can be helpful in ensuring, for example, that distributions are always positive.

LCIA Methods
============

Method metadata
---------------

There is a very basic set of metadata stored about each model, stored in the file ``methods.json``. To get the metadata about a method, do something like the following:

.. code-block:: python

    from brightway2 import *
    methods[(u'ecological scarcity 1997', u'total', u'total')]

.. note::
    See also the `methods manager documentation <http://bw2data.readthedocs.org/en/latest/technical.html#bw2data.meta.Methods>`_

The returned metadata is:

.. code-block:: python

    {u'abbreviation': u'ecologicals1997tt-UHk4Z8Pr',
     u'description': u'Swiss method',
     u'unit': u'UBP'}

Methods should have the following metadata:

    * *description*: A description of this method or submethod.
    * *unit*: The unit of this method or submethod.

In addition, the metadata ``abbreviation`` is generated automatically.

LCIA method documents
---------------------

The impact assessment method documents are quite simple - indeed, it is a bit of a stretch to call them documents at all. Instead, they are a list of biosphere flow references, characterization factors, and locations. All LCIA methods in Brightway2 are regionalized, though the default installed methods only provide global characterization factors. Here is a simple example:

.. code-block:: python

    from brightway2 import *
    Method(('ecological scarcity 1997', 'total', 'total')).load()[:5]

This returns the following:

.. code-block:: python

    [[(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1'), 32000, u'GLO'],
     [(u'biosphere', u'86a37cf9e44593f1c41fdce53de27715'), 32000, u'GLO'],
     [(u'biosphere', u'a8cc9c61aa343fa01532bb16cec7f90d'), 32000, u'GLO'],
     [(u'biosphere', u'b0a29177e77471a49b5a7d6a88212bf8'), 32000, u'GLO'],
     [(u'biosphere', u'72c1cf2fee31a2cb6cdc39abda29a0df'), 32000, u'GLO']]

Each list elements has two required components and a third optional component.

    #. A reference to a biosphere flow, e.g. ``(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1')``.
    #. The numeric characterization factor. This can either be a number, or a uncertainty dictionary (see :ref:`uncertainty-type`).
    #. An *optional* location, used for regionalized impact assessment. The global location ``GLO`` is inserted as a default if not location is specified.

.. note::
    LCIA method documents can be validated with ``bw2data.validate.ia_validator(my_data)``, or ``Method(("my", "method", "name")).validate(my_data)``.

Brightway2 LCA Reports
======================

.. note:: The Brightway2 report data format is evolving, and this section should not be understood as definitive.

LCA reports calculated with ``bw2analyzer.report.SerializedLCAReport`` are written as a JSON file to disk. It has the following data format:

.. code-block:: python

    {
        "monte carlo": {
            "statistics": {
                "interval": [lower, upper values],
                "median": median,
                "mean": mean
            },
            "smoothed": [  # This is smoothed values for drawing empirical PDF
                [x, y],
            ],
            "histogram": [  # This are point coordinates for each point when drawing histogram bins
                [x, y],
            ]
        },
        "score": LCA score,
        "activity": [
            [name, amount, unit],
        ],
        "contribution": {
            "hinton": {
                "xlabels": [
                    label,
                ],
                "ylabels": [
                    label,
                ],
                "total": LCA score,
                "results": [
                    [x index, y index, score], # See hinton JS implementation in bw2ui source code
                ],
            },
            "treemap": {
                "size:" LCA score,
                "name": "LCA result",
                "children": [
                    {
                    "name": activity name,
                    "size": activity LCA score
                    },
                ]
            }
            "herfindahl": herfindahl score,
            "concentration": concentration score
        },
        "method": {
            "name": method name,
            "unit": method unit
        },
        "metadata": {
            "version": report data format version number (this is 1),
            "type": "Brightway2 serialized LCA report",
            "uuid": the UUID of this report,
            "online": URL where this report can be accessed. Optional.
        }
    }

Brightway2 packages
===================

Brightway2 has a format for transferring data between computers, and for archiving data for more permanent storage. This format is called a *bw2package*, and is just JSON data compressed using the bzip2 algorithm.

Technical documentation is `provided in brightway2-data <http://bw2data.readthedocs.org/en/latest/io.html#bw2data.io.BW2Package>`_, but end users shouldn't need to know too much about this format.
