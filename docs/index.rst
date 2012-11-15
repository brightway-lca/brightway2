.. Brightway2 documentation master file, created by
   sphinx-quickstart on Tue Nov 13 15:32:29 2012.

Brightway2 life cycle assessment framework
==========================================

Brightway2 is a simple framework for life cycle assessment (LCA). Its focus is on efficient calculation and visualization. Brightway2 is a complete rewrite of the original Brightway, which was a previous LCA framework developed during the PhD thesis of Chris Mutel.

Fast LCA and Monte Carlo calculations
=====================================

The life cycle assessment calculators are the most advanced part of Brightway2. For those that are interested, a full technical guide is available. For the rest of you, suffice it to say that LCA calculations are powerful and efficient (working with LCI databases of hundreds of thousands of processes has been done successfully), and the Monte Carlo implementation allows for effective use of modern computers. On a semi-modern laptop, around 100 Monte Carlo iterations per core are possible, and each core can be used in parallel.

New data visualizations
=======================

(Include visualizations here)

Treemaps and Hinton matrices are already part of the standard LCA report, and new visualizations using the D3 library are planned. See the examples.

Simple data structure
=====================

Brightway2 uses a very simple data structure. Instead of a database, which is powerful but difficult to install or upgrade, Brightway2 uses a data directory, and saves data as Python datastructures serialized to normal files. The location of the data directory can be configured; default is in your home directory. Although this approach loses some of the benefits of relational databases, it has several advantages:

* No database installation or configuration.
* You can easily share your work with someone else by copying the data directory and sending it to your colleagues. Syncing services like dropbox can also be easily used.
* Copying, modifying, and backing up databases is easy and fast.

Documentation
=============

Table of contents:

.. toctree::
   :maxdepth: 2

   introduction
   databases
   querying
   technical

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

