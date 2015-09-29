.. image:: images/bw2logo.png
    :align: center

Brightway2 life cycle assessment framework
==========================================

Brightway2 is a open source framework for life cycle assessment (LCA). It is designed to be easy to use, while still being powerful. Brightway2 doesn't try to replace software like SimaPro or OpenLCA, but instead offers possibilities to those who need to go break the limits of conventional LCA. Brightway2 is especially attractive for researchers, especially when used with `IPython notebooks <http://ipython.org/notebook.html>`_. The core principles of Brightway2 are simplicity, innovation, and power.

Who is Brightway2 for?
----------------------

Brightway2 is for people who want more than is possible with current LCA or sustainability software. Researchers and academics are particularly suitable, because the power that Brightway2 brings is worth the cost of learning a new software and possibly a new language.

Brightway2 is not for people that want to do the same old LCA studies, just with a different software. If OpenLCA works for you now, stick with it. One particular weakness of Brightway2 is routine data entry, although there is an active project trying to make this better.

Basically, Brightway2 is for you if your project lies at the intersection of LCA and your imagination.

.. warning:: These instructions are for the development version of Brightway2 - some things might not work as intended! Please email cmutel@gmail.com with bug reports or frustrated desires. See also the list of :ref:`knownissues`

.. note:: Please subscribe to the `brightway2 updates mailing list <https://tinyletter.com/brightway2-updates>`__ to be informed of new releases.

Understanding the manual
------------------------

..
   .. note:: This manual is `available as a PDF <http://brightwaylca.org/Brightway2%20manual.pdf>`_ or `on the web <https://brightway2.readthedocs.org/en/latest/>`_.

.. note:: In addition to this manual, there is a `discussion mailing list <https://groups.google.com/forum/?fromgroups#!forum/brightway2>`_, and a `Brightway2 development blog <http://chris.mutel.org/>`_.

As this manual covers a lot of material, it can be a bit overwhelming, especially at first. The manual is designed to help you get started in the following order:

* First, :ref:`install Brightway2 <installation>` and set up a :ref:`notebook directory <notebook-directory>`.
* Second, read the :ref:`introduction to brightway2 concepts <intro>`.
* Third, look at some of the :ref:`example notebooks <example-notebooks>`.
* Finally, use the rest of the manual as a reference while creating next-generation LCA studies.

In addition to the main index page and table of contents, in the HTML version you can search the documentation in the box on the left, and look for specific terms in the :ref:`genindex` (if you are reading this as a PDF there is an index at the end of this document).

.. _knownissues:

Known issues
------------

* Improve test coverage
* Need methods to change ``database`` and ``code`` for activities (currently just raises an error)
* Manual has many outdated sections, and structure should be revamped

Users Manual
============

.. toctree::
   :maxdepth: 2

   installation
   intro
   notebooks
   io
   ui
   intermediate
   metadata
   uncertainty
   lci
   ia
   lca
   faq
   credits

Developers Manual
=================

.. toctree::
   :maxdepth: 2

   advanced-installation
   porting
   contributing
   packages

Technical Reference
===================

.. toctree::
   :maxdepth: 2

   technical/bw2data
   technical/bw2calc
   technical/bw2io
   technical/bw2analyzer
