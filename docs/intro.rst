.. _intro:

Introduction
============

Data structure
--------------

Brightway2 is a framework for life cycle assessment (LCA). The word framework was chosen carefully, and the most powerful way to use Brightway2 is as a component of something bigger you want to build.

The basic organization is hierarchical:

.. image:: images/org-scheme.png
    :align: center

At the top, we have projects. A project is a workspace with its own databases, LCI methods, and any other data you need. Each project is completely independent of other projects. In the file system, each project is its own subdirectory.

Inside a project we have a number of objects that store data. Some of this data can be specific to a project, and not LCA-specific at all. For example, data about how to link two different databases, or a database of vehicle registrations, could be used to prepare data for LCA calculations. However, the most common data objects as inventory *databases* and impact assessment *methods*.

The default way to store inventory databases is in a `SQLite <https://www.sqlite.org/>`__ database with two tables: activities and exchanges. What Brightway2 calls a database is a collection of nodes in the supply chain, and includes transforming activities, products, and biosphere flows, and activities and biosphere can be mixed in a single database. Both SimaPro projects and libraries would be databases in Brightway2.

Activities are identified by their database and ``code``. A code is a string of letters and numbers that uniquely identifies that activity within the database. The only other required fields for activities is their ``name``, but most activities will have a ``location`` and ``unit`` as well.

If no ``type`` is specified, then the activity is assumed to be a ``process``. Biosphere flows have the type ``biosphere``. Brightway2 allows activities to produce products, which are separate activity nodes with the type ``product``. Activity types are used to determine whether an activity should be placed in the biosphere or technosphere matrices.

Exchanges are links between two activities of any type. Exchanges have an ``input`` and an ``output``: ``input`` is the activity being consumed or produced, and ``output`` is the consumer or producer. Exchanges should also have an ``amount`` and a ``type``. Common types include ``technosphere``, ``biosphere``, and ``production``. Multiple exchanges between two activities are allowed, and will be summed together.

Many activities have a reference production, which is an exchange of type ``production`` where the ``input`` is the same as the ``output``. Brightway2 allows multioutput processes; you are responsible for making sure the final system can be solved (see `multioutput processes in LCA <http://chris.mutel.org/multioutput.html>`__).
