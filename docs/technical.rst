Technical guide
***************

Modular structure
=================

Brightway2 is a framework for life cycle assessment, and consists of several packages. You only need to install or understand the components that are of interest to you. Splitting components allow for a clean separation of concerns, as each package has a limited focus, and makes testing and documenting each package easier and cleaner. 

This guide has technical details for the ``brightway2`` package. Each separate package also has its own documentation.

The current components of Brightway2 are:

* brightway2: This package provides data handling, querying, and import/export functionality.
* brightway2-calc: The LCA calculators. Normal LCA, several varieties of Monte Carlo LCA (including parallel Monte Carlo using all the cores on your computer), Latin Hypercubic sampling, and graph traversal.
* brightway2-analyzer: Functions for analyzing the results of LCA calculations, including contribution and sensitivity analysis.
* brightway2-ui: Two different user interfaces for Brightway2. Brightway2 is pure Python, and can be used by other programs or in an ipython notebook. For people who aren't as comfortable programming in Python, this packages provides a command line interface for work in the terminal, and a web interface.
* brightway2-speedups: A few small utilities that can make calculations faster. Requires Cython.

Configuration
=============

The configuration for brightway2 (which is currently only the location of the data directory) is implemented as a singleton class that is created when ``brightway2`` is imported.

.. autoclass:: brightway2._config.Config
	:members:

Metadata
========

.. autoclass:: brightway2.meta.Databases
	:members:
	:inherited-members:

.. autoclass:: brightway2.meta.Methods
	:members:
	:inherited-members:

.. autoclass:: brightway2.meta.Mapping
	:members:
	:inherited-members:

Documentation
=============

Documentation is uses `Sphinx <http://sphinx.pocoo.org/>`_ to build the source files into other forms. Building is as simple as changing to the docs directory, and running ``make.bat html`` in Windows and ``make html`` in OS X and Linux.

Database
========

.. autoclass:: brightway2.Database
    :members:

Method
======

.. autoclass:: brightway2.Method
    :members:

Import and Export
=================

.. autoclass:: brightway2.io.EcospoldImporter
    :members:

.. autoclass:: brightway2.io.EcospoldImpactAssessmentImporter
    :members:
