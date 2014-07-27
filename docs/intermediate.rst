Intermediate and processed data
===============================

Both inventory datasets and impact assessment methods are stored as structured text files, but these files are not efficient when constructing the technosphere, biosphere, and characterization matrices. These text documents are stored in the ``intermediate`` folder. Brightway2 also has a ``processed`` folder, which stores only the data needed to construct the various computational matrices. These data are stored as `numpy structured arrays <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_.

For both databases and LCIA methods, the method ``.write(some_data)`` will write an *intermediate* data file, while the subsequent method ``.process()`` will transform the intermediate data file to an array. These two functions are intentionally separate, as it is sometimes desirable to do one and not the other.

A following section (:ref:`building-matrices`) describes how processed data are turned into matrices for LCA calculations.

.. warning::
    Every time you save a new version of an inventory database or an impact assessment method, e.g. with ``my_database.write(my_data)``, be sure to also call ``my_database.process()``, or your changes will not be used in LCA calculations.

Processing data
---------------

*Processing data* converts document data to a binary form tailored for creating matrices (a NumPy array). All extraneous information is removed, and only the numeric values needed are retained. Put another way, *processing* transforms unstructured data documents to a highly-structured binary form for calculations.

.. _mapping:

Mappings
--------

Sometimes, important data can't be stored as a numeric value, even when numeric values are required in the processed data arrays. For example, the location of an inventory activity is important for regionalization, but is given by a text string, not an integer. In this case, we create a special dictionary that maps each unique data value to an integer index. Brightway2 uses two such mappings:

    * :ref:`mapping <mapping>`: Maps inventory objects (activities, biosphere flows, and anything else that would appear in a supply chain graph) to indices.
    * :ref:`geomapping`: Map locations (both inventory and regionalized impact assessment) to indices.

Items are added to mappings using ``.add(keys)``, and removed using ``.delete(keys)``. However, managing the different mappings is done for you automatically.
