Contributing
============

.. note::
    See also :ref:`contact-developers` for information on the mailing list.

Brightway2 is designed to be easy to use and develop for. The modular structure of Brightway2 means that you don't have to learn everything at once - pick the subject that best suits your interests and skills, download the code, and start hacking!

Required packages
-----------------

In addition to the Brightway2 modules you want to work on, you should also install the following:

    * `nose <https://github.com/nose-devs/nose>`_: A library for finding and running tests.
    * `sphinx <http://sphinx-doc.org/>`_: A library for writing and formatting documentation.
    * `mercurial <http://mercurial.selenic.com/>`_: A distributed version control system.

This can be done easily. Try to install these packages through Canopy or anaconda, if you are using them. Otherwise, use pip:

.. code-block:: bash

    pip install nose sphinx mercurial

Using mercurial
~~~~~~~~~~~~~~~

Mercurial is a distributed version control system, which records changes made in your source code over time, and allows changes from multiple people to merged to a single code base. `hginit <http://hginit.com/>`_ is a good guide to get started with Mercurial.

Contributing changes to Brightway2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The preferred way to submit changes is with a pull request on Bitbucket. A pull request is a fancy way of saying "Hey! I made some changes to what you already had in my own playground over here - how about you merge my changes back into the main source code repository." The instructions on pull requests are slightly different for `Windows users <https://confluence.atlassian.com/display/BITBUCKET/Fork+a+Repo,+Compare+Code,+and+Create+a+Pull+Request>`_ and `OS X/Linux users <https://confluence.atlassian.com/pages/viewpage.action?pageId=271942986>`_. For small changes, and especially things like typos, you can even use the online text editor without having to download anything.

No Python needed - making graphics better
-----------------------------------------

One easy way of helping out that doesn't require any knowledge of Python, matrices, or even actually life cycle assessment at all, is to help make the existing graphics better or introduce new ones. Each graphic in the LCA report is also available in a online:

* `Treemap <http://tributary.io/inlet/4951698>`_
* `Hinton matrix <http://tributary.io/inlet/4951859>`_
* `Force-directed graph`_
* `Monte Carlo results <http://tributary.io/inlet/4951873>`_

The code here is editable, and the changes you make will be immediately reflected in the display. Feel free to make some tweaks, or even major changes, to make the visualizations nicer, easier to understand, and simpler. If you have for other graphics that would be useful in interpreting LCA results, or in exploring inventory datasets or impact assessment methods, feel free to :ref:`contact-developers` to get a sample dataset.

Principles for good code
~~~~~~~~~~~~~~~~~~~~~~~~

    * Follow the Zen of Python - if you don't know what this is, try typing ``import this`` in a python shell.
    * Follow style guides like `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_. Tools like `pylint <http://pypi.python.org/pypi/pylint>`_ can help.
    * Write tests, and check test coverage.
    * Use `sphinx <http://sphinx-doc.org/>`_ to write documentation while you are writing code.

Easy problems
-------------

Tune the force-directed graph parameters to avoid the "hairball" problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of parameters in the `Force-directed graph`_, such as link distance and circle radius, which can be tuned to make the graph easier to understand. Go ahead and try to change them a bit and see what happens!

Implement other graphs from D3.js
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some possibilities we could include in either LCA reports, or in exploring or analyzing inventory databases:

    * Database visualization
        * `Hive plots <http://bost.ocks.org/mike/hive/>`_
        * `Hierarchal edge modelling <http://mbostock.github.com/d3/talk/20111116/bundle.html>`_
        * `Sunburst partition <http://bl.ocks.org/4063423>`_
        * `Chord diagrams <http://bl.ocks.org/4062006>`_
    * Supply chain visualization
        * `Collapsible force-directed <http://mbostock.github.com/d3/talk/20111116/force-collapsible.html>`_
        * `Rheingold-Tilford tree <http://bl.ocks.org/4063550>`_
    * Other results visualization
        * `Circle packing <http://bl.ocks.org/4063530>`_
        * `Bubble chart <http://bl.ocks.org/4063269>`_

Improve report layout and CSS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Those who know a bit about design, or at least think that they do, are welcome to make the report page better. Here is an `example report page <http://reports.brightwaylca.org/report/fb20439529cb414784e25acb8b3ef426>`_.

Improve test coverage
~~~~~~~~~~~~~~~~~~~~~

Each of the three calculation packages has an `online report available <http://coverage.brightwaylca.org/>`_. Many of the test coverage failures can be easily resolved with simple tests, and writing simple tests is a great way to get started with Python and Brightway2.

Medium problems
---------------

Find holes in tests
~~~~~~~~~~~~~~~~~~~

Tests always have edge cases that weren't anticipated by the developers, and coverage doesn't test for exceptions. Finding these edge cases or exceptions is a thankless but extremely important part of making robust software.

Ecospold exporter
~~~~~~~~~~~~~~~~~

The base Brightway2 data format doesn't include fields for all of the Ecospold data format, but we can still export that data that is available in the Ecospold format. This would help in making Brightway2 data more transportable. It is not necessarily a difficult task, but writing a lot of XML processing code is never very much fun.

Improve the activity-browser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The existing `activity-browser <https://bitbucket.org/cmutel/activity-browser>`__ has a lot of potential, but still needs a lot of work.

Hard problems
-------------

Sankey flow diagram
~~~~~~~~~~~~~~~~~~~

Sankey diagrams are helpful for showing the flows of raw material inputs or environmental impact through the supply chain. There are some `initial ideas <http://blog.bitjuice.com.au/2013/02/using-d3-js-to-visualise-hierarchical-classification/>`_, see also `a simpler example <http://bost.ocks.org/mike/sankey/>`_ on how to do this in D3, but the problem here is actually twofold:

    #. Disaggregating the supply chain graph in a reasonable fashion without having it either collapse or retain too many deep links
    #. Graph layout and display of additional information in D3

.. _Force-directed graph: http://tributary.io/inlet/4681149

Playing well with others
------------------------

Because the data model of Brightway2 is relatively simple, there is a lot of potential for providing data, especially numerical data and matrices, in the formats needed by other programming languages. Here are some examples:

* Export matrices and do calculations in Matlab (see `exporting a sparse matrix to Matlab <http://stackoverflow.com/questions/21214659/exporting-a-scipy-sparse-matrix-from-python2-7-to-matlab>`_).
* Calling data management `functions in python <https://github.com/stevengj/PyCall.jl>`_, and then doing `calculations in Julia <http://julia.readthedocs.org/en/latest/stdlib/sparse/>`_.
* Exporting numerical data to raw binary formats, and then loading and doing calculations in a hip functional language like `scala <http://www.scala-lang.org/>`_ or `f# <http://fsharp.org/>`_.
