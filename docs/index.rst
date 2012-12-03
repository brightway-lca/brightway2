.. Brightway2 documentation master file, created by
   sphinx-quickstart on Tue Nov 13 15:32:29 2012.

Brightway2 life cycle assessment framework
==========================================

Brightway2 is a simple framework for life cycle assessment (LCA). Its focus is on efficient calculation and visualization. Brightway2 is a complete rewrite of the original Brightway, which was a previous LCA framework developed during the PhD thesis of Chris Mutel.

.. attention:: 
    Brightway2 is in heavy development, and while it is used by mutiple people every day, it is probably not ready for people who don't like digging into source code and filing bug reports.

Why another LCA framework?
==========================

Because existing LCA software is not very good at calculations. Brightway2 is not trying to replace software such as OpenLCA or SimaPro; rather, it is designed for individual analysts to be able to do cutting edge calculations on their computers, their servers, or in the cloud.

Features
========

Fast LCA and Monte Carlo calculations
-------------------------------------

The life cycle assessment calculators are the most advanced part of Brightway2. For those that are interested, a full technical guide is available. For the rest of you, suffice it to say that LCA calculations are powerful and efficient (working with LCI databases of hundreds of thousands of processes has been done successfully), and the Monte Carlo implementation allows for effective use of modern computers. On a semi-modern laptop, around 100 Monte Carlo iterations per core are possible, and each core can be used in parallel.

New data visualizations
-----------------------

(Include visualizations here)

Treemaps and Hinton matrices are already part of the standard LCA report, and new visualizations using the D3 library are planned. See the examples.

Simple data handling
--------------------

Brightway2 uses a very simple data structure. Instead of a database, which is powerful but difficult to install or upgrade, Brightway2 uses a data directory, and saves data as Python datastructures serialized to normal files. The location of the data directory can be configured; default is in your home directory. Although this approach loses some of the benefits of relational databases, it has several advantages:

* No database installation or configuration.
* You can easily share your work with someone else by copying the data directory and sending it to your colleagues. Syncing services like dropbox can also be easily used.
* Copying, modifying, and backing up databases is easy and fast.

Quick start
===========

This is the easiest way to get started using Brightway2 on **Windows**. If you are interested in using the full power of the Brightway2 framework, or are using **Mac OS X** or **Linux**, see other installation options (link).

First, download the latest version of `Python (x,y) <https://code.google.com/p/pythonxy/wiki/Downloads>`_, and install it. This is the easiest way to get the `NumPy <http://numpy.scipy.org/>`_ and `SciPy <http://scipy.org/>`_ libraries.

* `Python (x,y) <https://code.google.com/p/pythonxy/wiki/Downloads>`_

Second, download and install the XML processing library `lxml <http://pythonxy.googlecode.com/files/lxml-3.0.1-1_py27.exe>`_.

* `lxml <http://pythonxy.googlecode.com/files/lxml-3.0.1-1_py27.exe>`_

Third, open a command prompt (Start -> Run), and type in the following:

.. code-block:: bash
	
	pip install brightway2

Finally, again in the command prompt, start Brightway2:

.. code-block:: bash

	bw2-web.py

This should start the program, and open a new web browser tab to the correct address. Brightway2 will recognize that you are starting Brightway2 for the first time, and give you instructions on how to download basic data, import your projects, and start working.

Documentation
=============

Table of contents:

.. toctree::
   :maxdepth: 2

   installation
   introduction
   usage
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

