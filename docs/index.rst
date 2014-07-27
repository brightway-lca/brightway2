Brightway2 life cycle assessment framework
==========================================

Brightway2 is a open source framework for life cycle assessment (LCA). It is designed to be easy to use, while still being powerful. Brightway2 doesn't try to replace software like SimaPro or OpenLCA, but instead offers possibilities to those who need to go break the limits of conventional LCA. Brightway2 is especially attractive for researchers, especially when used with `IPython notebooks <http://ipython.org/notebook.html>`_. The core principles of Brightway2 are simplicity, innovation, and power.

Who is Brightway2 for?
----------------------

Brightway2 is for people who want more than is possible with current LCA or sustainability software. Researchers and academics are particularly suitable, because the power that Brightway2 brings is worth the cost of learning a new software and possibly a new language.

A particular weakness of Brightway2 is routine data entry, although there is an active project trying to make this better.

Basically, Brightway2 is for you if your project lies at the intersection of LCA and your imagination.

Understanding the manual
------------------------

.. note:: This manual is `also available as a PDF <http://brightwaylca.org/Brightway2%20manual.pdf>`_.

As this manual covers a lot of material, it can be a bit overwhelming, especially at first. The manual is designed to help you get started in the following order:

* First, :ref:`install Brightway2 <installation>` and its dependencies.
* Second, :ref:`configure Brightway2 <configuration>` by setting a data directory.
* Third, do the :ref:`five tutorials <five-tutorials>`.
* Finally, use the rest of the manual as a reference while creating next-generation LCA studies.

In addition to the main index page and table of contents, in the HTML version you can search the documentation in the box on the left, and look for specific terms in the :ref:`genindex`. There an index at the end of the LaTeX version, but it doesn't get linked correctly for some reason.

.. _installation:

Installation
============

Brightway2 can be installed pretty much everywhere, on Windows, OS X, Linux, and anywhere else Python can be compiled.

.. note:: Brightway2 is currently only compatible with python 2.7, not python 3. Work on Python 3 support is ongoing, but don't hold your breath.

.. toctree::
   :maxdepth: 2

   installation

.. _configuration:

Configuration
=============

Configuring Brightway2 is pretty easy - the only thing to do is to tell it where it can store data, logs, and exported files. We call this directory the "data directory", and its structure is explained in detail below. The first thing Brightway2 needs is to know where it can save data and log files. This directory location, in addition to a number of other configuration variables, is managed by the ``config`` object.

Configuration through the web interface
---------------------------------------

In a terminal shell or command prompt, type:

.. code-block:: bash

    bw2-web

.. image:: images/configuration-1.png
    :align: center

Brightway2 will determine that you are starting it for the first time. You will need to create a :ref:`data-directory` - a writable directory where all data will be stored.

    1. Click to open directories, and navigate to where you want the data directory to be created.
    2. Check to make sure the directory path is correct.
    3. Keep the default name for the data directory - ``brightway2`` - or choose your own.
    4. Click to create and populate the data directory.

.. image:: images/configuration-2.png
    :align: center

.. image:: images/configuration-3.png
    :align: center

Brightway2 comes with some basic metadata - LCIA methods and a biosphere database. They will be automatically downloaded.

.. image:: images/configuration-4.png
    :align: center

Configuration through the command line
--------------------------------------

Configuration can also be done with the command line utility ``bw2-controller``. Simply run the following command, and confirm that you want to create the data directory.

.. code-block:: bash

    bw2-controller setup --data-dir=/my/blank/directory

Configuration in a python shell
-------------------------------

The data directory can be set in the python shell, either permanently:

.. code-block:: python

    from brightway2 import set_data_dir
    set_data_dir("/path/to/directory")

or just for the current python session (useful if you have different data directories for each project):

.. code-block:: python

    from brightway2 import set_data_dir
    set_data_dir("/path/to/directory", permanent=False)

.. _five-tutorials:

Getting started
===============

The best way to get started is by going through the five tutorials. These are designed not to be read, but are IPython notebooks that can be executed on your computer.

* `Tutorial 1 - Getting Started <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%201%20-%20Getting%20Started.ipynb>`_
* `Tutorial 2 - Working with data <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%202%20-%20Working%20with%20data.ipynb>`_
* `Tutorial 3 - Basic LCA Calculations <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%203%20-%20Basic%20LCA%20Calculations.ipynb>`_
* `Tutorial 4 - Meta-analysis <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%204%20-%20Meta-analysis.ipynb>`_
* `Tutorial 5 - Defining A New Matrix <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%205%20-%20Defining%20A%20New%20Matrix.ipynb>`_

After doing the tutorials, you should have an idea of what is possible with Brightway2. The rest of the manual will help explain its components in more detail, but is not designed to be read through in one sitting. It is more of a reference work than a novel. You are ready to start exploring, and the manual will try to help you when you get lost.

User interfaces
===============

(I)Python shell
---------------

Brightway2 can be used from the interactive python shell. `IPython <http://ipython.org/>`_ is a nicer shell that adds shortcuts, shell commands, and a lot else.

IPython notebook
----------------

`IPython notebooks <http://ipython.org/notebook.html>`_ are the probably the best way to interact with Brightway2 (see the :ref:`five tutorials <five-tutorials>`). These lab notebooks open incredible possibilities for interactive, reproducible, collaborative, and understandable science. Read more about the `praise IPython has been getting <http://ipython.org/#announcements>`_, and see `some awesome demos <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`_. IPython notebooks are `not just for python <http://jupyter.org/>`_, either.

bw2-controller
--------------

``bw2-controller`` is a command line application that helps manage LCI databases and LCIA methods. Each time it is invoked, it does one action, and then exits. The following commands are available:

* *bw2-controller --help*: List the commands supported by ``bw2-controller``.
* *bw2-controller list databases*: List all LCI databases.
* *bw2-controller list methods*: List all LCIA methods.
* *bw2-controller details <name>*: Give details of database *name*.
* *bw2-controller copy <name> <newname>*: Copy database *name* to *newname*.
* *bw2-controller backup <name>*: Backup database *name*.
* *bw2-controller validate <name>*: Validate the datasets in database *name*.
* *bw2-controller versions <name>*: List the saved versions of database *name*.
* *bw2-controller revert <name> <revision>*: Revert database *name* to version *revision*.
* *bw2-controller remove <name>*: Delete database *name*.
* *bw2-controller export <name> [--include-dependencies]*: Export database <name>. Set *--include-dependencies* to include any databases linked by <name>.
* *bw2-controller setup*: Download default biosphere database and LCIA methods.
* *bw2-controller setup --data-dir=<datadir>*: Set the data directory permanently to <datadir>, and then download default biosphere database and LCIA methods.
* *bw2-controller upload_logs [COMMENT]*: Upload error logs to the Brightway2 server. Useful for helpign debug platform-specific errors.
* *bw2-controller color on*: Turn color output on.
* *bw2-controller color off*: Turn color output off. Sometimes the color library doesn't work perfectly.

bw2-browser
-----------

``bw2-browser`` is a command line application that allows you to interactively examine LCA datasets and databases. There is a `video explaining how it works <https://www.youtube.com/watch?v=Dw3s5K8OsM0>`_. After starting the activity browser by typing ``bw2-browser`` into a command shell or terminal, the following commands are available:

Basic commands:

* *?*: Print this help screen.
* *quit* or *q*: Exit the activity browser.
* *<number>*: Go to option <number>, when a list of options is present.
* *l*: List current options.
* *n*: Go to next page in paged options.
* *p*: Go to previous page in paged options.
* *p* number: Go to page number in paged options.
* *h*: List history of databases and activities viewed.
* *wh*: Write history to a text file.
* *autosave*: Toggle autosave behaviour on and off.

Working with databases:

* *ldb*: List available databases.
* *db <name>*: Go to database <name>. No quotes needed.
* *s <string>*: Search activity names in current database with <string>.

Working with activities:

* *a <id>*: Go to activity <id> in current database. Complex ids in quotes.
* *i*: Info on current activity.
* *web*: Open current activity in web browser. Must have ``bw2-web`` running.
* *r*: Choose a random activity from current database.
* *u*: List upstream activities (inputs for the current activity).
* *d*: List downstream activities (activities which consume current activity).
* *b*: List biosphere flows for the current activity.

bw2-web
-------

``bw2-web`` is a web user interface launched from the command line. To be honest, it is not great - it is OK for exploring methods and databases, and has what could be, with some work, a good LCA calculation report. However, it is convenient for some things, and will remain so until someone decides to make it better.

There isn't any specific documentation for ``bw2-web`` - just click on stuff and hope it doens't break.

.. _data-directory:

The data directory
==================

The data directory is a single directory where Brightway2 stores data, logs, exported files, and everything else it needs on disk.

Data directory structure
------------------------

The data directory has some metadata files, and a bunch of subdirectories for storing different kinds of data. Because it is a single directory, it is safe for backup programs or sync services like Dropbox.

A separate data directory can be created for each project. However, each data directory is self-contained, so each must contain a copy of all background databases and LCIA methods.

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

New subdirectories can be created using ``config.request_dir(new_dir_name)`` (see :ref:`configuration-technical`).

The ``config`` object in detail
-------------------------------

Configuration is managed by the :ref:`config <configuration-technical>` object: a `singleton <http://en.wikipedia.org/wiki/Singleton_pattern>`_ object instantiated the first time you import Brightway2. It stores the Brightway2 data directory, and has utility functions to change the data directory. It also stores information about whether or not it is being run on Windows, or used in an IPython shell. The ``config`` object can be imported from ``brightway2`` or ``bw2data``:

.. code-block:: python

    from brightway2 import config
    config.dir
    >> '/Users/cmutel/brightway2'

See also: the technical documentation for the :ref:`configuration-technical` object.

.. _user-preferences:

User preferences
----------------

The ``config`` object also stores user preferences. User preferences include things like the default number of Monte Carlo iterations to run, but it is just a dictionary, and can be added to as desired. Here are some common keys in the user preferences directory:

* "use_cache": Boolean. Store datasets in memory for faster access. Default is true.
* "global_location": String. Name of global location to use when no location was provided. Default is "GLO".
* "biosphere_database": String. Name of biosphere database. Default is "biosphere".
* "temp_dir_ok": Boolean. Allow work in the web UI while using a temporary directory. Default is false.
* "upload_reports": Boolean. If true, upload LCA reports generated by bw2analyzer to a reports web server. Default is false.
* "report_server_url": URL of the server to upload LCA reports. Default is 'http://reports.brightwaylca.org'
* "iterations": Integer. Default number of Monte Carlo iterations when calculating an LCA in the web UI. Default is 1000.
* "cpu_cores": Integer. Default number of CPU cores to use when calculating an LCA in the web UI. Default is the number of cores on the computer.

In addition, there are some values in the user preferences which are set automatically, and should not be changed manually:

* "ab_*": A set of values used by the activity browser UI
* "browser_*": A set of values used by the activity browser UI
* "updates": A list of which updates have been applied

.. warning:: Preferences are not saved automatically - you must call ``config.save_preferences()``.

How Brightway2 chooses the data directory
-----------------------------------------

.. note:: The data directory can be changed after Brightway2 is loaded with ``set_data_dir`` (see :ref:`set-data-dir`)

The first thing that Brightway2 will look for is the `environment variable <http://foo.bar>`_ ``BRIGHTWAY2_DIR``. If this is found, then it is the location of the ``data directory``. An environment variable is especially convenient if you have multiple copies of Brightway2 installed on one machine, or if you want to keep separate workspaces for different projects.

To set an environment variable:

    * Unix/Mac: ``export BRIGHTWAY2_DIR=/path/to/brightway2/directory``. Add this to your ``.profile`` or similar file to have this set each time you open a terminal window.
    * Windows 7/8: Use ``setx BRIGHTWAY2_DIR=\path\to\brightway2\directory`` to set an environment variable permanently. Power users should consider `SetEnv <http://www.codeproject.com/Articles/12153/SetEnv>`_.

The second thing that Brightway2 will try is a file called ``.brightway2path`` in your home directory. If this file is present, it should have one line, which is the directory location. No quoting or special characters are needed.

Because it can be difficult to work with so-called "dot-files" whose name starts with a ``.``, especially on Windows, Brightway2 will also try to read a file call ``brightway2path.txt`` in your home directory. This works the same as the ``.brightway2path`` file. If you set the data directory through the web interface or with ``bw2-controller``, it writes a ``.brightway2path`` or ``brightway2path.txt`` file.

Finally, Brightway2 will try to see if there is a writeable directory in your home directory called ``brightway2``.

If none of these attempts succeed, Brightway2 will create and user a temporary directory, but will complain about it, as these directories can be deleted by the operating system.

Intermediate and processed data
===============================

Both inventory datasets and impact assessment methods are stored as structured text files, but these files are not efficient when constructing the technosphere, biosphere, and characterization matrices. These text documents are stored in the ``intermediate`` folder. Brightway2 also has a ``processed`` folder, which stores only the data needed to construct the various computational matrices. These data are stored as `numpy structured arrays <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_.

For both databases and LCIA methods, the method ``.write(some_data)`` will write an *intermediate* data file, while the subsequent method ``.process()`` will transform the intermediate data file to an array. These two functions are intentionally separate, as it is sometimes desirable to do one and not the other.

A following section (:ref:`building-matrices`) describes how processed data are turned into matrices for LCA calculations.

.. warning::
    Every time you save a new version of an inventory database or an impact assessment method, e.g. with ``my_database.write(my_data)``, be sure to also call ``my_database.process()``, or your changes will not be used in LCA calculations.

Processing data
---------------

*Processing data* converts document data to a binary form tailored for creating matrices (a NumPy array). All extraneous information is removed, and only the numeric values needed are retained. Put another way, *processing* transforms unstructured data documents to a highly-structured binary form for calculations.

.. _mapping:

Mappings
--------

Sometimes, important data can't be stored as a numeric value, even when numeric values are required in the processed data arrays. For example, the location of an inventory activity is important for regionalization, but is given by a text string, not an integer. In this case, we create a special dictionary that maps each unique data value to an integer index. Brightway2 uses two such mappings:

    * :ref:`mapping <mapping>`: Maps inventory objects (activities, biosphere flows, and anything else that would appear in a supply chain graph) to indices.
    * :ref:`geomapping`: Map locations (both inventory and regionalized impact assessment) to indices.

Items are added to mappings using ``.add(keys)``, and removed using ``.delete(keys)``. However, managing the different mappings is done for you automatically.

.. _metadata-store:

Cataloging what we have - Metadata stores
=========================================

The building blocks in Brightway2 are LCI databases, LCIA methods, etc. However, we also need to keep track of which LCI databases and LCIA methods we have, and some additional information about them as a whole. For example, LCIA methods have units, and databases can have version numbers. A *metadata store* stores information about data objects like databases and methods.

The base class for metadata is :ref:`serialized-dict`, which is basically a normal dictionary that can be easily saved or loaded (i.e. serialized) to or from a `JSON <http://en.wikipedia.org/wiki/JSON>`_ file. These files can be easily edited in a normal text editor.

Brightway2 defines the following metadata stores:

* :ref:`databases`: LCI databases
* :ref:`methods`: LCIA methods (characterization factors)
* :ref:`normalizations`: LCIA normalization factors
* :ref:`weightings`: LCIA weighting factors

Metadata should be singletons
-----------------------------

There should be only one instance of each metadata store, to avoid having conflicting data (the `singleton pattern <http://en.wikipedia.org/wiki/Singleton_pattern>`_), though this is not enforced. The normal pattern is to instantiate each class in the same file as the class pattern:

.. code-block:: python

    class MyObjects(bw2data.serialization.SerializedDict):
        file = "sweet-peppers.json"

    myobjects = MyObjects()

Using metadata stores
---------------------

Most of the time, you will deal with the actual data objects. Metadata stores are mostly useful when examining which objects are available:

.. code-block:: python

   for name in databases:
      print name
   "a database name" in databases

Metadata stores are also used when deleting data objects:

.. code-block:: python

   del databases["some database to delete"]

Finally, metadata stores can be used to get metadata about data objects:

.. code-block:: python

   methods[methods.random()]
   >> {u'abbreviation': u'recipe-endpoint-ha-wo-lthc.0ba25d5fd76e35b3125224ce78d37151',
       u'unit': u'points'}

.. _uncertainty-type:

Storing uncertain values
========================

While some numeric data is certain, like unit conversions, real-world data is often uncertain. In Brightway2, uncertain data is stored in a ``uncertainty dictionary``.

An ``uncertainty dictionary`` is a python dictionary of keys and values, like:

.. code-bock:: python

   {
      "Swiss chesse": "is awesome",
      "this is a key": "this is a value"
   }

It has one required key: ``amount``, which specifies the most representative value of the distribution. The most representative value can be the mean, median (like in the lognormal in the ecoinvent database), mode (like in the triangular in the ecoinvent database), or something else - the decision is up to you. The uncertainty distribution is defined by the key ``uncertainty type``.  Depending on the distribution, some or all of the following fields can also be specified: *loc*, *scale*, *shape*, *minimum*, and *maximum*.

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

The default value for ``uncertainty type`` is ``0``, i.e. no uncertainty.

.. note::
    All distributions (where bounds make sense) can be bounded, i.e. you can specify a minimum and maximum value in addition to other parameters. This can be helpful in ensuring, for example, that distributions are always positive.

In most cases, if you don't have uncertainty, or don't know enough to be able to characterize that uncertainty, you can enter a number instead of an uncertainty dictionary, and it will be automatically converted to an uncertainty dictionary with no uncertainty.

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

Brightway2 includes some simple functions for searching within databases. Because a database is a simple Python dictionary, it is relatively simple to filter and process. The strategy is to apply one (or more) ``Filter`` in a ``Query``. The return value of a ``Query`` is a ``Result``, which can printed or sorted. Queries can also be called directly from the ``Database`` object. Here is a simple example:

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

Impact Assessment
=================

In Brightway2, each impact assessment method is a set of characterization factors for a set of biosphere flows. Each impact category and subcategory is a separate method, and each method is stored and calculated separately.

Methods are identified by a list of names, which could be as simple as:

.. code-block:: python

    ("I scream", "you scream", "we all scream", "for ice cream")

which is probably most applicable for those who are particularly concerned with ice cream resource depletion; a more typical example is:

.. code-block:: python

    ('ecological scarcity 1997', 'total', 'total')

Impact assessment method names can have any length and number of qualifiers, but must always be a list of strings.

.. warning::
    For technical reasons, impact assessment names must be stored as a `tuple <http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences>`_, not a `list <http://docs.python.org/2/tutorial/introduction.html#lists>`_, i.e. they must have ``()`` at the beginning and end, and not ``[]``.

Method metadata
---------------

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

Default LCIA methods
--------------------

Starting Brightway2 through the web interface, or when you run ``bw2setup()`` in a python shell, Brightway2 will install around 650 default LCIA methods, as provided by the ecoinvent center. These LCIA methods will work for both ecoinvent 2 and 3.

LCA calculations
================

Normal static LCA
-----------------

The actual LCA class (``bw2calc.LCA``) is more of a coordinator then an accountant, as the matrix builder is doing much of the data manipulation. The :ref:`lca` class only has to do the following:

    * Translate the functional unit into a demand array
    * Find the right parameter arrays, and ask matrix builder for matrices
    * Solve the linear system :math:`Ax=B` using `SuperLU <http://crd-legacy.lbl.gov/~xiaoye/SuperLU/>`_ or `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_.
    * Multiply the result by the LCIA CFs, if a LCIA method is present

.. note:: Due to licensing conflicts, recent versions of SciPy do not include UMFpack. Python wrappers for UMFpack must be installed separately using `scikits.umfpack <https://github.com/stefanv/umfpack>`_.

The LCA class also has some convenience functions for redoing some calculations with slight changes, e.g. for uncertainty and sensitivity analysis. See the "redo_*" and "rebuild_*" methods in the LCA class.

.. _building-matrices:

Turning processed data arrays in matrices
-----------------------------------------

A parameter array is a NumPy `structured or record array <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_, where each column has a label and data type. Here is an sample of the parameter array for the US LCI:

======= ======= =========== =========== ======= ======
input   output  row         col         type    amount
======= ======= =========== =========== ======= ======
9829    9829    4294967295  4294967295  0       1.0
9708    9708    4294967295  4294967295  0       1.0
9633    9633    4294967295  4294967295  0       1.0
9276    9276    4294967295  4294967295  0       3.0999
8778    8778    4294967295  4294967295  0       1.0
9349    9349    4294967295  4294967295  0       1000.0
5685    9349    4294967295  4294967295  2       14.895
9516    9349    4294967295  4294967295  1       1032.7
9433    9349    4294967295  4294967295  1       4.4287
8838    9349    4294967295  4294967295  1       1.5490
======= ======= =========== =========== ======= ======

As this is a parameter array for a LCI database, it gives values that will be inserted into the technosphere and biosphere matrices, i.e. values from the dataset exchanges.

There are also some columns for uncertainty information, but these would only be a distraction for now. The complete spec for the uncertainty fields is given in the `stats_arrays documentation <http://stats-arrays.readthedocs.org/en/latest/>`_.

We notice several things:

    * Both the ``input`` and ``output`` columns have numbers, but we don't know what they mean yet
    * Both the ``row`` and ``col`` columns are filled with a large number
    * The `type`` column has only a few values, but they are also mysterious
    * The `amount` column is the only one that seems reasonable, and gives the values that should be inserted into the matrix

Input and Output
~~~~~~~~~~~~~~~~

The ``input`` and ``output`` columns gives values for biosphere flows or transforming activity data sets. :ref:`mapping` are used to translate keys like ``("Douglas Adams", 42)`` into integer values. So, each mapping number uniquely identifies an activity dataset.

If the ``input`` and ``output`` values are the same, then this is a production exchange - it describes how much product is produced by the transforming activity dataset.

.. warning:: Integer mapping ids are not transferable from machine to machine or installation to installation, as the order of insertion (and hence the integer id) is more or less at random. Always process new datasets.

Rows and columns
~~~~~~~~~~~~~~~~

The ``row`` and ``col`` columns have the data type *unsigned integer, 32 bit*, and the maximum value is therefore :math:`2^{32} - 1`, i.e. 4294967295. This is just a dummy value telling Brightway2 to insert better data.

The method ``MatrixBuilder.build_dictionary`` is used to take ``input`` and ``output`` values, respectively, and figure out which rows and columns they correspond to. The actual code is succinct - only one line - but what it does is:

    #. Get all unique values, as each value will appear multiple times
    #. Sort these values
    #. Give them integer indices, starting with zero

For our example parameter array, the dictionary from ``input`` values to ``row`` would be:

.. code-block:: python

    {5685: 0,
     8778: 1,
     8838: 2,
     9276: 3,
     9349: 4,
     9433: 5,
     9516: 6,
     9633: 7,
     9708: 8,
     9829: 9}

And the dictionary from ``output`` to ``col`` would be:

.. code-block:: python

    {8778: 0,
     9276: 1,
     9349: 2,
     9633: 3,
     9708: 4,
     9829: 5}

The method ``MatrixBuilder.add_matrix_indices`` would replace the 4294967295 values with dictionary values based on ``input`` and ``output``. At this point, we have enough to build a sparse matrix using ``MatrixBuilder.build_matrix``:

=== === ======
row col amount
=== === ======
9   5   1.0
8   4   1.0
7   3   1.0
3   1   3.0999
1   0   1.0
4   2   1000.0
0   2   14.895
6   2   1032.7
5   2   4.4287
2   2   1.5490
=== === ======

Indeed, the `coordinate (coo) matrix <http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.coo_matrix.html>`_ takes as inputs exactly the row and column indices, and the values to insert.

Of course, there are some details for specific matrices - technosphere matrices need to be square, and should have ones by default on the diagonal, etc. etc., but this is the general idea.

Types
~~~~~

The ``type`` column indicates whether a value should be in the technosphere or biosphere matrix: ``0`` is a transforming activity production amount, ``1`` is a technosphere exchange, and ``2`` is a biosphere exchange.

Stochastic LCA
--------------

The various stochastic Monte Carlo LCA classes function almost the same as the static LCA, and reuse most of the code. The only change is that instead of building matrices once, `random number generators from stats_arrays <http://stats-arrays.readthedocs.org/en/latest/mcrng.html#monte-carlo-random-number-generator>`_ are instantiated directly from each parameter array. For each Monte Carlo iteration, the ``amount`` column is then overwritten with the output from the random number generator, and the system solved as normal. The code to do a new Monte Iteration is quite succinct:

.. code-block:: python

    def next(self):
        self.rebuild_technosphere_matrix(self.tech_rng.next())
        self.rebuild_biosphere_matrix(self.bio_rng.next())
        if self.lcia:
            self.rebuild_characterization_matrix(self.cf_rng.next())

        self.lci_calculation()

        if self.lcia:
            self.lcia_calculation()
            return self.score
        else:
            return self.supply_array

This design is one of the most elegant parts of Brightway2.

Because there is a common procedure to build static and stochastic matrices, any matrix can easily support uncertainty, e.g. not just LCIA characterization factors, but also weighting, normalization, and anything else you can think of; see `tutorial 5: defining a new matrix <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%205%20-%20Defining%20A%20New%20Matrix.ipynb>`_.

Brightway2 LCA Reports
----------------------

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

Graph traversal
---------------

To generate graphs of impact like supply chain or Sankey diagrams, we need to traverse the graph of the supply chain. The ``GraphTraversal`` class does this in a relatively intelligent way, assessing each inventory activity only once regardless of how many times it is used, and prioritizing activities based on their LCA score. It is usually possible to create a reduced graph of the supply chain, with only the most relevant pathways and flows included, in a few seconds.

Illustration of graph traversal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It's easiest to understand how graph traversal is implemented with a simple example. Take this system:

.. image:: images/gt-system.png
    :align: center

* This system has four **nodes**, which are LCI processes, also called transforming activities. Each **node** has one reference product, and a set of zero or more technosphere inputs. By convention, node ``A`` produces one unit of product ``A``.
* This system has four **edges** which define the inputs of each node. An edge has a start, an end, and an amount.
* We consider solving this system for a *functional unit* of one unit of ``A``.

As we traverse this supply chain, we will keep different data for the nodes and the edges. For nodes, we are interested in the following:

* ``amount``: The total amount of this node needed to produce the functional unit.
* ``cum``: The cumulative LCA impact score attributable to the needed amount of this node, *including it's specific supply chain*.
* ``ind``: The individual  LCA impact score directly attributable to one unit of this node, i.e. the score from the direct emissions and resource consumption of this node.

For edges, we want to know:

* ``to``: The **id** of the node consuming the product.
* ``from``: The **id** of the node producing the product.
* ``amount``: The total amount of product ``from`` needed for the amount of ``to`` needed.
* ``exc_amount``: The amount of ``from`` needed for *one unit* of ``to``, i.e. the value given in the technosphere matrix.
* ``impact``: The total LCA impact score embodied in this edge, i.e. the individual score of ``from`` times ``amount``.

Our functional unit is one unit of ``A``. Before starting any calculations, we need to set up our data structures. First, we have an empty list of **edges**. We also have a **heap**, a list which is automatically sorted (see documentation on priority queue below), and keeps track of the **nodes** we need to examine. **nodes** are identified by their row index in the *technosphere matrix*. Finally, we have a dictionary of **nodes**, which looks up nodes by their id numbers.

.. code-block:: python

    nodes, edges, heap = {}, [], []

We create a special node, the functional unit, and insert it into the nodes dictionary:

.. code-block:: python

    nodes[-1] = {
        'amount': 1,
        'cum': total_lca_score,
        'ind': 1e-6 * total_lca_score
    }

The *cumulative LCA impact score* is obviously the total LCA score; we set the *individual LCA score* to some small but non-zero value so that it isn't deleted in graph simplification later on.

We next start building our list of edges. We start with all the inputs to the *functional unit*, which in this case is only one unit of ``A``. Note that the functional unit can have multiple inputs.

.. code-block:: python

    for node_id, amount in functional_unit:
        edges.append({
            "to": -1,  # Special id of functional unit
            "from": node_id,
            "amount": amount,  # By definition
            "exc_amount": amount,  # By definition
            "impact": LCA(node_id, amount).score,  # Evaluate LCA impact score for this node_id and amount
        })

Finally, we push each node to the **heap**:

.. code-block:: python

    for node_id, amount in functional_unit:
        heappush(heap, (abs(1 / LCA(node_id, amount).score), node_id))

This is not so easy to understand at first glance. What is ``1 / LCA(node_id, amount).score``? Why the absolute value? What is this ``heappush`` thing?

We want one *divided by* the LCA impact score for node ``A`` because our **heap** is sorted in ascending order, and we want the highest score to be first.

We take the absolute value because we are interested in the magnitude of node scores in deciding which node to process next, not the sign of the score - leaving out the absolute value would put all negative scores at the top of the heap (which is sorted in ascending order).

``heappush`` is just a call to push something on to the **heap**, which is our automatically sorted list of nodes to examine.

After this first iteration, we have the following nodes and edges in our graph traversal:

.. image:: images/gt-step-1.png
    :align: center

.. code-block:: python

    nodes = {-1: {'amount': 1, 'cum': some number, 'ind': some small number}}
    edges = [{
        'to': -1,
        'from': 0,  # Assuming A is 0
        'amount': 1,
        'exc_amount': 1,
        'impact': some number
    }]
    heap = [(some number, 0)]

After this is it rather simple: pull off the next node from the *heap*, add it to the list of nodes, construct its edges, and add its inputs to the heap. Iterate until no new nodes are found.

.. image:: images/gt-step-2.png
    :align: center

There are two more things to keep in mind:

* We use a cutoff criteria to stop traversing the supply chain - any node whose cumulative LCA impact score is too small is not added to the heap.
* We only visit each node once. The is functionality in ``bw2analyzer`` to "unroll" the supply chain so that each process can occur more than once.

Frequently Asked Questions
==========================

.. toctree::
   :maxdepth: 2

   faq

Contributing
============

.. note::
    See also :ref:`contact-developers` for information on the mailing list.

Brightway2 is designed to be easy to use and develop for. The modular structure of Brightway2 means that you don't have to learn everything at once - pick the subject that best suits your interests and skills, download the code, and start hacking!

.. toctree::
   :maxdepth: 2

   contributing

.. _packages:

Brightway2 Packages
===================

Brightway2 is split into several packages, where each package fulfills a certain role in the framework. The idea is that you can be an expert on a certain package, but not have to learn anything about other packages.

Core packages
-------------

brightway2-data
~~~~~~~~~~~~~~~

This package provides facilities for managing LCI databases and LCIA methods, as well as input and output scripts.

* `source code <https://bitbucket.org/cmutel/brightway2-data>`_
* `documentation <https://bw2data.readthedocs.org/en/latest/>`_
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/data/index.html>`_

brightway2-calc
~~~~~~~~~~~~~~~

This package provides classes for LCA calculations, both static and uncertain, and basic regionalized LCA.

* `source code <https://bitbucket.org/cmutel/brightway2-calc>`_
* `documentation <https://brightway2-calc.readthedocs.org/en/latest/>`_
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/calc/index.html>`_

brightway2-analyzer
~~~~~~~~~~~~~~~~~~~

This package provides functions for interpreting and analyzing LCI databases, LCIA methods, and LCA results.

* `source code <https://bitbucket.org/cmutel/brightway2-analyzer>`_
* `documentation <https://bw2analyzer.readthedocs.org/en/latest/>`_
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/analyzer/index.html>`_

brightway2-ui
~~~~~~~~~~~~~

This package provides both command line and web user interfaces.

* `source code <https://bitbucket.org/cmutel/brightway2-ui>`_

Secondary packages
------------------

These packages are extensions to Brightway2, and have lower standards for documentation and test coverage. They show how Brightway2 can be extended into new areas of LCA.

brightway2-regional
~~~~~~~~~~~~~~~~~~~

Full-fledged regionalization in Brightway2.

* `source code <https://bitbucket.org/cmutel/brightway2-regional>`_
* `documentation <https://brightway2-regional.readthedocs.org/en/latest/>`_

brightway2-temporalis
~~~~~~~~~~~~~~~~~~~~~

Dynamic LCA in Brightway2.

* `source code <https://bitbucket.org/cmutel/brightway2-temporalis>`_
* `documentation <https://brightway2-temporalis.readthedocs.org/en/latest/>`_

brightway2-restapi
~~~~~~~~~~~~~~~~~~

A simple `REST <http://en.wikipedia.org/wiki/Representational_state_transfer>`_ `API <http://en.wikipedia.org/wiki/Application_programming_interface>`_ for Brightway2 LCI data.

* `source code <https://bitbucket.org/cmutel/brightway2-restapi>`_
* `documentation <http://brightway2-restapi.readthedocs.org/en/latest/>`_
* `100% test coverage <http://coverage.brightwaylca.org/restapi/index.html>`_

brightway2-simple
~~~~~~~~~~~~~~~~~

Easier use of Brightway2 objects in the python shell/ipython notebook.

* `source code <https://bitbucket.org/cmutel/brightway2-simple>`_
* `documentation <http://brightway2-simple.readthedocs.org/en/latest/>`_
* `video <https://www.youtube.com/watch?v=n0UN9nj_mag>`_

Credits & License
=================

Authors
-------

Brightway2 was developed by `Chris Mutel <http://chris.mutel.org/>`_.

Additional contributers:

* `Bernhard Steubing <http://www.ifu.ethz.ch/ESD/people/bsteubin>`_
* `Niko Heeren <http://www.ifu.ethz.ch/staff/nheeren/index_EN>`_
* `Aurelian Jaggi <http://eaternity.ch/team/Aurelian-Jaggi/>`_
* `lowks <https://bitbucket.org/lowks>`_

.. _contact-developers:

Contact the developers
----------------------

Brightway2 has a mailing list: brightway2@googlegroups.com. You can register at the `Google groups site <https://groups.google.com/forum/?fromgroups#!forum/brightway2>`_.

You can also email Chris directly at ``cmutel@gmail.com``.

License
-------

Brightway2 is licensed under the `BSD license <http://opensource.org/licenses/BSD-3-Clause>`_.

::

    Copyright (c) 2014, Chris Mutel and ETH Zürich
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

    Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer. Redistributions in binary
    form must reproduce the above copyright notice, this list of conditions and the
    following disclaimer in the documentation and/or other materials provided
    with the distribution.

    Neither the name of ETH Zürich nor the names of its contributors may be used
    to endorse or promote products derived from this software without specific
    prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Technical Reference
===================

.. toctree::
   :maxdepth: 2

   technical/bw2data
   technical/bw2calc
   technical/bw2analyzer
