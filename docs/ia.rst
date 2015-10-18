Impact Assessment
=================

In Brightway2, each impact assessment method is a set of characterization factors for a set of biosphere flows. Each impact category and subcategory is a separate method, and each method is stored and calculated separately.

Methods are identified by a list of names, which could be as simple as:

.. code-block:: python

    ("I scream", "you scream", "we all scream", "for ice cream")

which is probably most applicable for those who are particularly concerned with ice cream resource depletion; a more typical example is:

.. code-block:: python

    ('ecological scarcity 1997', 'total', 'total')

Impact assessment method names can have any length and number of qualifiers - there is nothing special or sacred about three levels - but must always be a list of strings.

.. warning::
    For technical reasons, impact assessment names must be stored as a `tuple <http://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences>`_, not a `list <http://docs.python.org/2/tutorial/introduction.html#lists>`_, i.e. they must have ``()`` at the beginning and end, and not ``[]``.

Method metadata
---------------

Method metadata is a normal dictionary, and is indexed in the ``methods`` object. The object ``methods`` is a special dictionary that saves itself
whenever values change, but is otherwise still a normal dictionary.
``new_method.metadata`` is an alias for ``methods``. So, to change the metadata, do:

.. code-block:: python

    methods[('foo',)] = {'bar': True, ...}

Or to chance a single value:

.. code-block:: python

    methods[('IPCC 2007', 'climate change', 'GWP 100a')]['timeframe'] = 100

Note that after changing a single value, you will need to flush the
changes to disk:


.. code-block:: python

    methods.flush()

Methods should have the following metadata:

    * *description*: A description of this method or submethod.
    * *unit*: The unit of this method or submethod.

In addition, the metadata ``abbreviation`` is generated automatically.

LCIA method documents
---------------------

The impact assessment method documents are quite simple - indeed, it is a bit of a stretch to call them documents at all. Instead, they are a list of biosphere flow references, characterization factors, and locations. All LCIA methods in Brightway2 are regionalized, though the default installed methods only provide global characterization factors. Here is a simple example:

.. code-block:: python

    from brightway2 import *
    Method(('ecological scarcity 1997', 'total', 'total')).load()[:5]

This returns the following:

.. code-block:: python

    [[(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1'), 32000, u'GLO'],
     [(u'biosphere', u'86a37cf9e44593f1c41fdce53de27715'), 32000, u'GLO'],
     [(u'biosphere', u'a8cc9c61aa343fa01532bb16cec7f90d'), 32000, u'GLO'],
     [(u'biosphere', u'b0a29177e77471a49b5a7d6a88212bf8'), 32000, u'GLO'],
     [(u'biosphere', u'72c1cf2fee31a2cb6cdc39abda29a0df'), 32000, u'GLO']]

Each list elements has two required components and a third optional component.

    #. A reference to a biosphere flow, e.g. ``(u'biosphere', u'21c70338ff2e1cdc8e468f4c90f113a1')``.
    #. The numeric characterization factor. This can either be a number, or a uncertainty dictionary (see :ref:`uncertainty-type`).
    #. An *optional* location, used for regionalized impact assessment. The global location ``GLO`` is inserted as a default if not location is specified.

.. note::
    LCIA method documents can be validated with ``bw2data.validate.ia_validator(my_data)``, or ``Method(("my", "method", "name")).validate(my_data)``.

Default LCIA methods
--------------------

Starting Brightway2 through the web interface, or when you run ``bw2setup()`` in a python shell, Brightway2 will install around 650 default LCIA methods, as provided by the ecoinvent center. These LCIA methods will work for both ecoinvent 2 and 3.
