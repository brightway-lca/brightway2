Searching databases
*******************

Brightway2 includes some simple functions for searching within databases. Because a database is a simple Python dictionary, it is relatively simple to filter and process. The strategy is to apply one (or more) ``Filter`` in a ``Query``. The return value of a ``Query`` is a ``Result``, which can printed or sorted. Queries can also be called directly from the ``Database`` object. Here is a simple example:

.. code-block:: python

    In [1]: from brightway2.query import *
    In [2]: from brightway2 import *
    In [3]: ei = Database("ecoinvent 2.2")
    In [4]: r = ei.query(Filter("name", "in", "at long-distance pipeline"))
    In [5]: len(r)
    Out[5]: 8

    In [6]: print r
    Query result with 8 entries

    In [7]: r
    Out[7]: 
    Query result: (total 8)
    ('ecoinvent 2.2', 1427): natural gas, production DZ, at long-distance pipeline
    ('ecoinvent 2.2', 1425): natural gas, production DE, at long-distance pipeline
    ('ecoinvent 2.2', 1413): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1412): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1432): natural gas, production RU, at long-distance pipeline
    ('ecoinvent 2.2', 1431): natural gas, production NO, at long-distance pipeline
    ('ecoinvent 2.2', 1430): natural gas, production NL, at long-distance pipeline
    ('ecoinvent 2.2', 1429): natural gas, production GB, at long-distance pipeline

    In [8]: r.sort("name")
    In [9]: r
    Out[9]: 
    Query result: (total 8)
    ('ecoinvent 2.2', 1413): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1412): natural gas, at long-distance pipeline
    ('ecoinvent 2.2', 1425): natural gas, production DE, at long-distance pipeline
    ('ecoinvent 2.2', 1427): natural gas, production DZ, at long-distance pipeline
    ('ecoinvent 2.2', 1429): natural gas, production GB, at long-distance pipeline
    ('ecoinvent 2.2', 1430): natural gas, production NL, at long-distance pipeline
    ('ecoinvent 2.2', 1431): natural gas, production NO, at long-distance pipeline
    ('ecoinvent 2.2', 1432): natural gas, production RU, at long-distance pipeline

    In [10]: q = Query(Filter("unit", "iis", "tkm"), Filter("name", "in", "lorry"))
    In [11]: r = q(ei.load())
    In [12]: len(r)
    Out[12]: 19

Filter
======

.. autoclass:: brightway2.Filter
    :members:

Query
=====

.. autoclass:: brightway2.Query
    :members:

Result
======

.. autoclass:: brightway2.Result
	:members:
