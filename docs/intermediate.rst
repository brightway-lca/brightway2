Intermediate and processed data
===============================

Both inventory datasets and impact assessment methods are stored as structured text files, stored in the ``intermediate`` folder. These files are not efficient when constructing the technosphere, biosphere, and characterization matrices. Brightway2 also has a ``processed`` folder, which stores only the data needed to construct the various computational matrices. These data are stored as `numpy structured arrays <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_.

For both databases and LCIA methods, the method ``.write(some_data)`` will write an *intermediate* data file, while the subsequent method ``.process()`` will transform the ``intermediate data`` file to an array. All extraneous information is removed, and only the numeric values needed are retained. Put another way, *processing* transforms unstructured data documents to a highly-structured binary form for calculations. ``write`` and ``process`` are intentionally separate, as it is sometimes desirable to do one and not the other.

:ref:`building-matrices` describes how processed data are turned into matrices for LCA calculations.

.. warning::
    Every time you save a new version of an inventory database or an impact assessment method, e.g. with ``my_database.write(my_data)``, be sure to also call ``my_database.process()``, or your changes will not be used in LCA calculations.

.. _processing-data:

Processing data
---------------

*Processing data* converts document data to a binary form tailored for creating matrices (a NumPy array).

.. _mappings:

Mappings
--------

Some LCA data is not numerical, like locations and dataset codes. We need numerical representations of these values to construct the processed data arrays, however. In this case, we create a special dictionary that maps each unique data value to an integer index. Brightway2 uses two such mappings:

    * :ref:`mapping <mapping>`: Maps inventory objects (activities, biosphere flows, and anything else that would appear in a supply chain graph) to indices.
    * :ref:`geomapping`: Map locations (both inventory and regionalized impact assessment) to indices.

Items are added to mappings using ``.add(keys)``, and removed using ``.delete(keys)``. However, managing the different mappings is done for you automatically.
