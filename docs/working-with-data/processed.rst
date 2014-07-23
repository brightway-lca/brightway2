Intermediate and processed data
*******************************

Both inventory datasets and impact assessment methods are stored as structured text files, but these files are not efficient when constructing the technosphere, biosphere, and characterization matrices. These text documents are stored in the ``intermediate`` folder. Brightway2 also has a ``processed`` folder, which stores only the data needed to construct the various computational matrices. These data are stored as `numpy structured arrays <http://docs.scipy.org/doc/numpy/user/basics.rec.html>`_.

For both databases and LCIA methods, the method ``.write(some_data)`` will write an *intermediate* data file, while the subsequent method ``.process()`` will transform the intermediate data file to an array. These two functions are intentionally separate, as it is sometimes desirable to do one and not the other.

.. warning::
    Every time you save a new version of an inventory database or an impact assessment method, e.g. with ``my_database.write(my_data)``, be sure to also call ``my_database.process()``, or your changes will not be used in LCA calculations.
