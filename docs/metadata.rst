.. _metadata-store:

Cataloging what we have - Metadata stores
=========================================

The building blocks in Brightway2 are LCI databases, LCIA methods, etc. However, we also need to keep track of which LCI databases and LCIA methods we have, and some additional information about them as a whole. For example, LCIA methods have units, and databases can have version numbers. A *metadata store* stores information about data objects like databases and methods.

The base class for metadata is :ref:`serialized-dict`, which is basically a normal dictionary that can be easily saved or loaded (i.e. serialized) to or from a `JSON <http://en.wikipedia.org/wiki/JSON>`_ file. These files can be easily edited in a normal text editor.

Brightway2 defines the following metadata stores:

* :ref:`databases`: LCI databases
* :ref:`methods`: LCIA methods (characterization factors)
* :ref:`normalizations`: LCIA normalization factors
* :ref:`weightings`: LCIA weighting factors

Metadata should be singletons
-----------------------------

There should be only one instance of each metadata store, to avoid having conflicting data (the `singleton pattern <http://en.wikipedia.org/wiki/Singleton_pattern>`_), though this is not enforced. The normal pattern is to instantiate each class in the same file as the class pattern:

.. code-block:: python

    class MyObjects(bw2data.serialization.SerializedDict):
        file = "sweet-peppers.json"

    myobjects = MyObjects()

Using metadata stores
---------------------

Most of the time, you will deal with the actual data objects. Metadata stores are mostly useful when examining which objects are available:

.. code-block:: python

   for name in databases:
      print name
   "a database name" in databases

Metadata stores are also used when deleting data objects:

.. code-block:: python

   del databases["some database to delete"]

Finally, metadata stores can be used to get metadata about data objects:

.. code-block:: python

   methods[methods.random()]
   >> {u'abbreviation': u'recipe-endpoint-ha-wo-lthc.0ba25d5fd76e35b3125224ce78d37151',
       u'unit': u'points'}
