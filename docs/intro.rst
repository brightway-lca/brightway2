.. _intro:

Introduction
============

Brightway2 is a framework for life cycle assessment (LCA). The word framework was chosen carefully, and the most powerful way to use Brightway2 is as a component of something bigger you want to build.

The basic organization is hierarchical:

.. image:: images/org-scheme.png
    :align: center

At the top, we have projects. A project is a workspace with its own databases, LCI methods, and any other data you need. Each project is completely independent of other projects. In the file system, each project is its own subdirectory.

Inside a project we have a number of objects that store data. Some of this data can be specific to a project, and not LCA-specific at all. For example, data about how to link two different databases, or a database of vehicle registrations, could be used to prepare data for LCA calculations. However, the most common data objects as inventory *databases* and impact assessment *methods*.

The default way to store inventory databases is in a SQLite3 database with two tables: activities and exchanges.
