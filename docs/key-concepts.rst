Key concepts
************

.. _data-directory:

Data directory
==============

All Brightway2 data is stored in a data directory, but the location of the directory can be chosen by the user. The data directory is just a bunch of subdirectories and files, so it is safe for backup programs or sync services like Dropbox.

Structure
---------

::

    data directory
        files:
            geomapping.pickle - Listing of all locations in all databases and methods
            mapping.pickle ---- Listing of all activities in all LCI databases
            databases.json ---- Metadata about LCI databases
            methods.json ------ Metadata about LCIA methods
            normalizations.json Metadata about LCIA normalizations
            preferences.json -- User settings
            weightings.json --- Metadata about LCIA weightings
        subdirectories:
            backups ----------- Directory for LCI database backups
            downloads --------- Location where downloaded data is stored
            intermediate ------ Directory where LCI database and LCIA method documents are stored
            logs -------------- Logs of Brightway2 activity
            processed --------- Compressed numerical arrays made from LCI and LCIA documents
            reports ----------- Data from LCA calculations

Data directory location
-----------------------

.. note::
    You can ignore all these technical details if you create a file called ``brightway2`` in your home directory, and don't want to do anything fancy.

The user can specify the ``data directory`` location in any of three different ways. In all cases, the directory should already exist. The first thing that Brightway will look for is the `environment variable <http://foo.bar>`_ ``BRIGHTWAY2_DIR``. If this is found, then it is the location of the ``data directory``. An environment variable is especially convenient if you have multiple copies of Brightway2 installed on one machine, or if you want to keep separate workspaces for different projects.

To set an environment variable:

    * Unix/Mac: ``export BRIGHTWAY2_DIR=/path/to/brightway2/directory``. Add this to your ``.profile`` or similar file to have this set each time you open a terminal window.
    * Windows 7: Use ``setx BRIGHTWAY2_DIR=\path\to\brightway2\directory`` to set an environment variable permanently.

The second thing that Brightway2 will try is a file called ``.brightway2path`` in your home directory. If this file is present, it should have one line, which is the directory location. No quoting or special characters are needed.

Because it can be difficult to work with so-called "dot-files", whose name starts with a ``.``, Brightway2 will also try to read a file call ``brightway2path.txt`` in your home directory. This works the same as the ``.brightway2path`` file.

Finally, Brightway2 will try to see if there is a writeable directory in your home directory called ``brightway2``.

If none of these attempts succeed, Brightway2 will work in a temporary directory, but will complain about it, as these directories can be deleted by the operating system.

Databases
=========

In Brightway2, a ``database`` is the term used to organize a set of activity datasets. Databases can be big, like ecoinvent, or as small as one dataset. You can have as many databases as you like, and databases can link into other databases. You can also have two databases that each depend on each other.

.. _biosphere-database:

Biosphere database
------------------

When Brightway2 is set up, it downloads and installs a special ``biosphere`` database. This database has all the resource and emission flows from the ecoinvent database, and is the database that imported life cycle impact assessment methods will link to.

You can define biosphere flows - resources and emissions - in any database you like, but it is probably best to use the pre-defined flows in the ``biosphere`` database whenever you can. If you need to add some custom flows, feel free to create a separate new database.

Documents
---------

An activity dataset is a document - just some text, with a minial amount of formatting. For example, here is a Brightway2 activity dataset from the US LCI:

.. code-block:: python

    {'categories': ['biomass', 'fuels'],
     'exchanges': [{
       'amount': 11968.25,
       'code': 7,
       'comment': 'From gasoline',
       'group': 2,
       'input': ('biosphere', '6d336c64e3a0ff08dee166a1dfdf0946'),
       'type': 'biosphere',
       'uncertainty type': 0}],
     'location': 'RNA',
     'name': 'Energy, output',
     'type': 'process',
     'unit': 'megajoule'}

There are some elements which might seem mysterious, and some elements which just make sense. I hope that things like ``name`` and ``unit`` don't need any explanation. The list of ``exchanges`` might be a bit more difficult to understand at first, because there are some weird fields like ``code`` and ``group`` which are left over from the import process. Actually, the list of required fields is quite small.

.. note::
    The details of the data format are described in :ref:`database-documents`

Here are the important points about activity datasets being documents:

    * They are a section of human-readable data that you can manipulate manually in a text editor, or change en masse programmatically.
    * Because they can be exported as text, and in a format that is accessible to almost every computer language (`JSON <http://www.json.org/>`_), activity datasets can be easily exported and used by other programs without spending hour messing around with XML which is constructed slightly differently by each LCA program.
    * Activity datasets have a small number of required fields, but allow any additional information you would like to add, so that it is easy to add whatever custom data you need for your application. #TODO: Examples

.. _dataset-codes:

Dataset codes
-------------

Linking activity datasets within and between databases requires a way to uniquely identify each dataset. Brightway uses the idea that each dataset has a unique code. A code can be a number, like ``1``, or a string of numbers and letters, like ``swiss ch33se``. When you create datasets manually, you will need to assign each dataset a code. When you import a database, the codes will be automatically generated for you.

Activity hashes
---------------

When you import an *ecospold* dataset, the codes that are generated automatically look like a bunch of nonsense, like this: ``6d336c64e3a0ff08dee166a1dfdf0946``. Although the *ecospold* format does include numbers, and some producers of ecoinvent use those numbers in a meaningful way, every other program that produces *ecospold* messes the numbers up, and so we can't believe them.

We want to have a way of identifying datasets which is consistent from machine to machine, so that it is easier to share and work with datasets without have to relink activities. The way Brightways identifies an activity or flow is with the `MD5 <http://en.wikipedia.org/wiki/MD5>`_ hash of a few attributes: the ``name``, ``location``, ``unit``, and ``categories``. The function is ``bw2data.utils.activity_hash``, but the procedure is simple: concatenate the name, each category, the unit and the location, all as lower-case strings. If an attribute doesn't have a value, ignore it. Then take the `MD5 <http://en.wikipedia.org/wiki/MD5>`_ hash of the resulting string.

.. _exchanges:

Exchanges
---------

Exchanges are a list of the inputs and outputs of an activity. For example an activity might consume some resources, emit some emissions, and have other technoligcal goods as emissions. Each activity also has at least one technological output.

Each exchange has a ``type``, which indicates where the exchange goes to or comes from. The predefined types are as follows:

    * ``production``: How much of the main output is produced by this dataset. A ``production`` exchange is not required, and when absent, a default value of 1 is used.
    * ``technosphere``: An input of a technological flow.
    * ``biosphere``: A consumption of a resource, or an emission to the environment. These flows are normally from the :ref:`biosphere-database`.

Brightway2 cannot, by itself, directly handle multi-output activities. However, you can include multi-output activites with substitution (see #TODO), and the **ecospold** importer will allocate multi-output datasets. This lack of support for multi-output datasets is due to Brightway2 being centered on matrix-calculations, which require a square technosphere matrix. If each dataset did not have precisely one output, the technosphere matrix would be rectangular, and therefore not generally solvable.

Impact assessment methods
=========================

In Brightway2, each impact assessment method is a set of characterization factors for a set of biosphere flows. Each impact category and subcategory is a separate method, and each method is stored and calculated separately.

Methods are identified by a list of names, which could be as simple as:

.. code-block:: python

    ("my new cool method for ice cream",)

which is probably most applicable for those who are particularly concerned with ice cream resource depletion; a more typical example is:

.. code-block:: python

    (u'ecological scarcity 1997', u'total', u'total')

Impact assessment method names can have any length and number of qualifiers, but must always be a list of strings.

.. warning::
    For technical reasons, impact assessment names must be stored as a `tuple <http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences>`_, not a `list <http://docs.python.org/2/tutorial/introduction.html#lists>`_, i.e. they must have ``()`` at the beginning and end, and not ``[]``.

Data formats
============

Pickle is the default data storage format
-----------------------------------------

Why is the Python standard library module `pickle <http://docs.python.org/2/library/pickle.html>`_ as the local data storage format?

The ``pickle`` module is fast, portable, and built-in. While using compression (such as gzip and bzip2) would reduce the size of the saved files, it also dramatically increases loading and saving times, by a factor of 3 - 30, depending on the test. Overall, the speed of ``pickle`` `seems to be fine <http://kbyanc.blogspot.ch/2007/07/python-serializer-benchmarks.html>`_.

The ``marshal`` module is faster - 40% faster writing, 25% faster reading - but produces files twice as big, and can change from computer to computer or even when Python is upgraded. The costs and potential risks of ``marshal`` overwhelm its speed gains.

Unlike ``JSON``, ``pickle`` can save all Python objects, and is consistently faster when considering all target operating systems. Moreover, ``pickle`` is part of the standard library, so no additional installation is necessary. There does not appear to be one standard ``JSON`` library, see e.g. `anyjson <http://pypi.python.org/pypi/anyjson/>`_, `yajl <http://pypi.python.org/pypi/yajl>`_, and `ujson <http://pypi.python.org/pypi/ujson/>`_, in addition to the builtin.

Some metadata is serialized to JSON
-----------------------------------

`JSON <http://www.json.org/>`_ is a great format for data interchange, and for humans to edit. Some metadata, such as the LCI databases and LCIA methods installed, and user preferences, are stored in JSON. These are files that humans might want to change manually, so it makes sense for them to be easy to edit. These files are also relatively small, and could be accessed by other programming languages.

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

    {u'depends': [u'biosphere'],
     u'version': 1}

Databases have the following metadata:

    * *depends*: A list of database names that this database links into and depends upon.
    * *version*: The integer version number of this database. Each time a database is saved this number is automatically incremented.

.. _database-documents:

Database documents
------------------

A database consists of inventory datasets, and inventory datasets have a required form and a number of required fields. However, these requirements form a minimum needed for LCA calculations - you can always add extra fields as needed by your application.

Here is a selection from an example dataset from the US LCI:

.. code-block:: python

    {'categories': ['Wood Product Manufacturing',
      'Softwood Veneer and Plywood Mnf.'],
     'code': 1,
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
     'location': 'RNA',
     'name': 'Green veneer, at plywood plant, US PNW',
     'type': 'process',
     'unit': 'kilogram'}

The document structure is:

    * *name* (string): Name of this activity.
    * *type* (string): One of ``production``, ``biosphere``, or ``technosphere``, but you can add custom types. See :ref:`exchanges`.
    * *categories* (list of strings, optional): A list of categories and subcategories. Can have any length.
    * *location* (string, optional): A location identifier. Default is *GLO*.
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

.. note::
    Technological ``exchanges`` are a list of **inputs**.

.. note::
    There should be a maximum of **one** ``production`` exchange.

.. note::
    Database documents can be validated with ``bw2data.validate.db_validator(my_data)``, or ``Database("my database name").validate(my_data)``.

.. _uncertainty-type:

Uncertainty types
-----------------

.. note::
    All distributions (where it is applicable) can be bounded, i.e. you can specify and minimum and maximum value in addition to other parameters. This can be helpful in ensuring, for example, that distributions are always postive.

The integer *uncertainty type* fields are defined in a separate software package called `bw-stats-toolkit <https://bitbucket.org/cmutel/bw-stats-toolkit>`_. The uncertainty types are:

    * ``0``: Undefined uncertainty. Does not vary.
    * ``1``: No uncertainty. Does not vary.
    * ``2``: Lognormal distribution. This is **purposely** handled in an inconsistent fashion, unfortunately. The ``amount`` field is the median of the data, and the ``sigma`` field is the standard deviation of the data **when it is log-transformed**, i.e. the σ from the formula for the log-normal PDF.
    * ``3``: Normal distribution. ``amount`` is the mean, and ``sigma`` is the standard deviation.
    * ``4``: Uniform distribution. Picks values between ``minimum`` and ``maximum``.
    * ``5``: Triangular distribution. Picks values between ``minimum`` and ``maximum``, with a mode of ``amount``.
    * ``6``: Bernoulli distribution. ``amount`` is the cutoff between yes and no. ``maximum`` and ``minimum`` can rescale the interval away from (0, 1).
    * ``7``: `Discrete uniform <http://en.wikipedia.org/wiki/Uniform_distribution_(discrete)>`_ distribution picks integer values between ``minimum`` and ``maximum``.
    * ``10``: Beta distribution. ``amount`` is α, and ``sigma`` is β. ``maximum`` is a scaling parameter.

LCIA method metadata
--------------------

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

Methods have the following metadata:

    * *abbreviation*: Becuase LCIA methods have long and complicated names, Brightway2 abbreviates them to get a safe filename to save the data.
    * *description*: A description of this method or submethod.
    * *unit*: The unit of this method or submethod.

LCIA method documents
---------------------

The impact assessment method documents are quite simple - indeed, it is a bit of a stretch to call them documents at all. Instead, they are a list of biosphere flow references, characterization factors, and locations. All LCIA methods in Brightway2 are regionalized, though the default installed methods only provide global characterization factors. Here is a simple example:

.. code-block:: python

    from brightway2 import *
    Method((u'ecological scarcity 1997', u'total', u'total')).load()[:5]

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
    #. An optional location, used for regionalized impact assessment. The global location ``GLO`` is inserted as a default if not location is specified.

.. note::
    LCIA method documents can be validated with ``bw2data.validate.ia_validator(my_data)``, or ``Method(("my", "method", "name")).validate(my_data)``.

Intermediate and processed data
-------------------------------

Both inventory datasets and impact assessment methods are stored as structured text files, but these files are not efficient when constructing the technosphere, biosphere, and characterization matrices. These text documents are stored in the ``intermediate`` folder. Brightway2 also has a ``processed`` folder, which stores only the data needed to construct the various computational matrices. These data are stored as `numpy structured arrays <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_.

For both databases and LCIA methods, the method ``.write(some_data)`` will write an *intermediate* data file, while the subsequent method ``.process()`` will transform the intermediate data file to an array. These two functions are intentionally separate, as it is sometimes desirable to do one and not the other.

.. warning::
    Every time you save a new version of an inventory database or an impact assessment method, e.g. with ``my_database.write(my_data)``, be sure to also call ``my_database.process()``, or your changes will not be used in LCA calculations.

Reports
-------

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

Data interchange & archiving
----------------------------

Brightway2 has a format for transferring data between computers, and for archiving data for more permanent storage. This format is called a *bw2package*, and is just JSON data compressed using the bzip2 algorithm.
