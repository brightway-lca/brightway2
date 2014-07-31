Brightway2 life cycle assessment framework
==========================================

Brightway2 is a open source framework for life cycle assessment (LCA). It is designed to be easy to use, while still being powerful. Brightway2 doesn't try to replace software like SimaPro or OpenLCA, but instead offers possibilities to those who need to go break the limits of conventional LCA. Brightway2 is especially attractive for researchers, especially when used with `IPython notebooks <http://ipython.org/notebook.html>`_. The core principles of Brightway2 are simplicity, innovation, and power.

Who is Brightway2 for?
----------------------

Brightway2 is for people who want more than is possible with current LCA or sustainability software. Researchers and academics are particularly suitable, because the power that Brightway2 brings is worth the cost of learning a new software and possibly a new language.

Brightway2 is not for people that want to do the same old LCA studies, just with a different software. If OpenLCA works for you now, stick with it. One particular weakness of Brightway2 is routine data entry, although there is an active project trying to make this better.

Basically, Brightway2 is for you if your project lies at the intersection of LCA and your imagination.

Understanding the manual
------------------------

.. note:: This manual is `available as a PDF <http://brightwaylca.org/Brightway2%20manual.pdf>`_ or `on the web <https://brightway2.readthedocs.org/en/latest/>`_.

.. note:: In addition to this manual, there is a `discussion mailing list <https://groups.google.com/forum/?fromgroups#!forum/brightway2>`_, and a `Brightway2 development blog <http://chris.mutel.org/>`_.

As this manual covers a lot of material, it can be a bit overwhelming, especially at first. The manual is designed to help you get started in the following order:

* First, :ref:`install Brightway2 <installation>` and its dependencies.
* Second, :ref:`configure Brightway2 <configuration>` by setting a data directory.
* Third, do the :ref:`five tutorials <five-tutorials>`.
* Finally, use the rest of the manual as a reference while creating next-generation LCA studies.

In addition to the main index page and table of contents, in the HTML version you can search the documentation in the box on the left, and look for specific terms in the :ref:`genindex`. If you are reading this as a PDF, ``genindex`` isn't a link, but there is an index at the end of this document.

Brightway2 Manual
=================

.. toctree::
   :maxdepth: 3

   installation
   configuration
   tutorials
   ui
   data-directory
   intermediate
   metadata
   uncertainty
   lci
   ia
   lca
   faq
   contributing
   packages
   credits

Technical Reference
===================

.. toctree::
   :maxdepth: 3

   technical/bw2data
   technical/bw2calc
   technical/bw2analyzer
