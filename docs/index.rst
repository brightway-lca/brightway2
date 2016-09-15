.. image:: images/bw2logo.png
    :align: center

Brightway2 life cycle assessment framework
==========================================

Brightway2 is a open source framework for life cycle assessment (LCA). It is designed to be easy to use, while still being powerful. Brightway2 doesn't try to replace software like SimaPro or OpenLCA, but instead offers possibilities to those who need to go break the limits of conventional LCA. Brightway2 is especially attractive for researchers, especially when used with `Jupyter notebooks <http://jupyter.org/>`__. The core principles of Brightway2 are simplicity, innovation, and power.

Who is Brightway2 for?
----------------------

Brightway2 is for people who want more than is possible with current LCA or sustainability software. Researchers and academics are particularly suitable, because the power that Brightway2 brings is worth the cost of learning a new software and possibly a new language.

Brightway2 is not for people that want to do the same old LCA studies, just with a different software. If OpenLCA works for you now, stick with it. One particular weakness of Brightway2 is routine data entry, although there is an active project trying to make this better.

Basically, Brightway2 is for you if your project lies at the intersection of LCA and your imagination.

What's new?
-----------

* July 2016: Instructions for running Brightway2 on the :ref:`cloud`, including an official `Brightway2 Docker instance <https://hub.docker.com/r/cmutel/brightway2/>`__.

Understanding the manual
------------------------

As this manual covers a lot of material, it can be a bit overwhelming, especially at first. The manual is designed to help you get started in the following order:

* Install Brightway (:ref:`Windows quickstart <quick-windows-install>` or :ref:`otherwise <advanced-installation>`) and set up a :ref:`notebook directory <notebook-directory>`.
* Read the :ref:`introduction to brightway2 concepts <intro>`.
* Look at some of the :ref:`example notebooks <example-notebooks>`.
* Use the rest of the manual as a reference while creating next-generation LCA studies. If you need additional help, you can search the documentation (search box is on the left), or look in the :ref:`genindex`.

This manual is `available as a PDF <https://docs.brightwaylca.org/Brightway2-manual.pdf>`_.

Other resources
---------------

* Ask `Brightway2 questions on Stack Overflow <http://stackoverflow.com/questions/tagged/brightway?sort=newest>`__ (note: tag is `brightway`).
* `Brightway2 development blog <http://chris.mutel.org/>`__

Users Manual
============

.. toctree::
   :maxdepth: 2

   installation
   advanced-installation
   intro
   notebooks
   cloud
   ui
   lca
   faq
   issues
   contributing
   credits

Technical Reference
===================

.. toctree::
   :maxdepth: 2

   technical/bw2data
   technical/bw2calc
   technical/bw2io
   technical/bw2analyzer
