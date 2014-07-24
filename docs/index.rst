Brightway2 life cycle assessment framework
==========================================

Brightway2 is a open source framework for life cycle assessment (LCA). It is designed to be easy to use, while still being powerful. Brightway2 doesn't try to replace software like SimaPro or OpenLCA, but instead offers possibilities to those who need to go break the limits of conventional LCA. Brightway2 is especially attractive for researchers, especially when used with `iPython notebooks <http://ipython.org/notebook.html>`_. The core principles of Brightway2 are simplicity, innovation, and power.

Simplicity
----------

Large and complex software is hard to test for correctness, hard to work with, and hard to improve. Brightway2 is designed to be simple in every aspect: each major element is split into a separate software package, making it easier to understand and test; lean data structures make it easier to focus only on what is truly important; a user interface with fewer functions makes it easy to find the right button, and hard to make mistakes.

Innovation
----------

Power
-----


Who is Brightway2 for?
----------------------

Understanding the manual
------------------------

.. note:: This manual is `also available as a PDF <http://brightwaylca.org/Brightway2%20manual.pdf>`_.

As this manual covers a lot of material, it can be a bit overwhelming, especially at first. In addition to the main index page and table of contents, in the HTML version you can search the documentation in the box on the left, and look for specific terms in the :ref:`genindex`. There an index at the end of the LaTeX version, but it doesn't get linked correctly for some reason.

Installation
============

Brightway2 can be installed pretty much everywhere, on Windows, OS X, Linux, and anywhere else Python can be compiled.

.. note:: Brightway2 is currently only compatible with python 2.7, not python 3. Work on Python 3 support is ongoing, but don't hold your breath.

.. toctree::
   :maxdepth: 2

   installation

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

Getting started
===============

The best way to get started is by going through the five tutorials. These are designed not to be read, but are iPython notebooks that can be executed on your computer.

* `Tutorial 1 - Getting Started <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%201%20-%20Getting%20Started.ipynb>`_
* `Tutorial 2 - Working with data <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%202%20-%20Working%20with%20data.ipynb>`_
* `Tutorial 3 - Basic LCA Calculations <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%203%20-%20Basic%20LCA%20Calculations.ipynb>`_
* `Tutorial 4 - Meta-analysis <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%204%20-%20Meta-analysis.ipynb>`_
* `Tutorial 5 - Defining A New Matrix <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%205%20-%20Defining%20A%20New%20Matrix.ipynb>`_

After doing the tutorials, you should have an idea of what is possible with Brightway2. The rest of the manual will help explain its components in more detail, but is not designed to be read through in one sitting. It is more of a reference work than a novel. You are ready to start exploring, and the manual will try to help you when you get lost.

Working with data
=================

.. toctree::
   :maxdepth: 2

   working-with-data/saving-data
   working-with-data/databases
   working-with-data/data-formats
   working-with-data/processed

.. _data-directory:

The data directory
==================

Data directory structure
------------------------

All Brightway2 data is stored in a single directory, the location of which is chosen by the user. The data directory has some metadata files, and a bunch of subdirectories for storing different kinds of data. Because it is a single directory, it is safe for backup programs or sync services like Dropbox.

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

New subdirectories can be created using ``config.request_dir`` (see :ref:`configuration-technical`).

The ``config`` object in detail
-------------------------------

Configuration is managed by the ``config`` object: a `singleton <http://en.wikipedia.org/wiki/Singleton_pattern>`_ object instantiated the first time you import brightway2. It stores the Brightway2 data directory, and has utility functions to change the data directory. It also stores information about whether or not it is being run on Windows, or used in an iPython shell. The ``config`` object can be imported from ``brightway2`` or ``bw2data``:

.. code-block:: python

    from brightway2 import config
    config.dir
    >> '/Users/cmutel/brightway2'

See also: the technical documentation for the :ref:`configuration-technical` object.

User preferences
----------------

The ``config`` object also stores user preferences. User preferences include things like the default number of Monte Carlo iterations to run, but it is just a dictionary, and can be added to as desired.

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

LCI Databases
=============

.. toctree::
   :maxdepth: 2

   databases/index

Import and Export
=================

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

Static LCA
==========

The actual LCA class then is more of a coordinator then an accountant, as the matrix builder is doing much of the data manipulation. The :ref:`lca` class only has to do the following:

    * Translate the functional unit into a demand array
    * Find the right parameter arrays, and ask matrix builder for matrices
    * Solve the linear system :math:`Ax=B` using `SuperLU <http://crd-legacy.lbl.gov/~xiaoye/SuperLU/>`_ or `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_.
    * Multiply the result by the LCIA CFs, if a LCIA method is present

.. note:: Due to licensing conflicts, recent versions of SciPy do not include UMFpack. Python wrappers for UMFpack must be installed separately using `scikits.umfpack <https://github.com/stefanv/umfpack>`_.

The LCA class also has some convenience functions for redoing some calculations with slight changes, e.g. for uncertainty and sensitivity analysis. See the "redo_*" and "rebuild_*" methods in the LCA class.

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

The ``input`` and ``output`` columns gives values for biosphere flows or transforming activity data sets. Brightway2-data uses a `mapping dictionary <http://bw2data.readthedocs.org/en/latest/metadata.html#bw2data.meta.Mapping>`_ to translate keys like ``("Douglas Adams", 42)`` into integer values. So, each number uniquely identifies an activity dataset.

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
==============

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

Graph traversal
===============

To generate graphs of impact like supply chain or Sankey diagrams, we need to traverse the graph of the supply chain. The ``GraphTraversal`` class does this in a relatively intelligent way, assessing each inventory activity only once regardless of how many times it is used, and prioritizing activities based on their LCA score. It is usually possible to create a reduced graph of the supply chain, with only the most relevant pathways and flows included, in a few seconds.

Illustration of graph traversal
-------------------------------

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

Credits
=======

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
