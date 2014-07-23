Static LCA
==========

The actual LCA class then is more of a coordinator then an accountant, as the matrix builder is doing much of the data manipulation. The :ref:`lca` class only has to do the following:

    * Translate the functional unit into a demand array
    * Find the right parameter arrays, and ask matrix builder for matrices
    * Solve the linear system :math:`Ax=B` using `UMFpack <http://www.cise.ufl.edu/research/sparse/umfpack/>`_
    * Multiply the result by the LCIA CFs, if a LCIA method is present

The LCA class also has some convenience functions for redoing some calculations with slight changes, e.g. for uncertainty and sensitivity analysis. See the "redo_*" and "rebuild_*" methods in the LCA class.

Stochastic LCA
==============

The various stochastic Monte Carlo LCA classes function almost the same as the static LCA, and reuse most of the code. The only change is that instead of building matrices once, `random number generators from stats_arrays <http://stats-arrays.readthedocs.org/en/latest/mcrng.html#monte-carlo-random-number-generator>`_ are instantiated directly from each parameter array. For each Monte Carlo iteration, the ``amount`` column is then overwritten with the output from the random number generator, and the system solved as normal. The code to do a new Monte Iteration is quite succinct:

.. code-block:: python

    def next(self):
        self.rebuild_technosphere_matrix(self.tech_rng.next())
        self.rebuild_biosphere_matrix(self.bio_rng.next())
        if self.lcia:
            self.rebuild_characterization_matrix(self.cf_rng.next())

        self.lci_calculation()

        if self.lcia:
            self.lcia_calculation()
            return self.score
        else:
            return self.supply_array

This design is one of the most elegant parts of Brightway2.

Because there is a common procedure to build static and stochastic matrices, any matrix can easily support uncertainty, e.g. not just LCIA characterization factors, but also weighting, normalization, and anything else you can think of; see `tutorial 5: defining a new matrix <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial%205%20-%20Defining%20A%20New%20Matrix.ipynb>`_.

Graph traversal
===============

To generate graphs of impact like supply chain or Sankey diagrams, we need to traverse the graph of the supply chain. The ``GraphTraversal`` class does this in a relatively intelligent way, assessing each inventory activity only once regardless of how many times it is used, and prioritizing activities based on their LCA score. It is usually possible to create a reduced graph of the supply chain, with only the most relevant pathways and flows included, in a few seconds.

Illustration of graph traversal
-------------------------------

It's easiest to understand how graph traversal is implemented with a simple example. Take this system:

.. image:: images/gt-system.png
    :align: center

* This system has four **nodes**, which are LCI processes, also called transforming activities. Each **node** has one reference product, and a set of zero or more technosphere inputs. By convention, node ``A`` produces one unit of product ``A``.
* This system has four **edges** which define the inputs of each node. An edge has a start, an end, and an amount.
* We consider solving this system for a *functional unit* of one unit of ``A``.

As we traverse this supply chain, we will keep different data for the nodes and the edges. For nodes, we are interested in the following:

* ``amount``: The total amount of this node needed to produce the functional unit.
* ``cum``: The cumulative LCA impact score attributable to the needed amount of this node, *including it's specific supply chain*.
* ``ind``: The individual  LCA impact score directly attributable to one unit of this node, i.e. the score from the direct emissions and resource consumption of this node.

For edges, we want to know:

* ``to``: The **id** of the node consuming the product.
* ``from``: The **id** of the node producing the product.
* ``amount``: The total amount of product ``from`` needed for the amount of ``to`` needed.
* ``exc_amount``: The amount of ``from`` needed for *one unit* of ``to``, i.e. the value given in the technosphere matrix.
* ``impact``: The total LCA impact score embodied in this edge, i.e. the individual score of ``from`` times ``amount``.

Our functional unit is one unit of ``A``. Before starting any calculations, we need to set up our data structures. First, we have an empty list of **edges**. We also have a **heap**, a list which is automatically sorted (see documentation on priority queue below), and keeps track of the **nodes** we need to examine. **nodes** are identified by their row index in the *technosphere matrix*. Finally, we have a dictionary of **nodes**, which looks up nodes by their id numbers.

.. code-block:: python

    nodes, edges, heap = {}, [], []

We create a special node, the functional unit, and insert it into the nodes dictionary:

.. code-block:: python

    nodes[-1] = {
        'amount': 1,
        'cum': total_lca_score,
        'ind': 1e-6 * total_lca_score
    }

The *cumulative LCA impact score* is obviously the total LCA score; we set the *individual LCA score* to some small but non-zero value so that it isn't deleted in graph simplification later on.

We next start building our list of edges. We start with all the inputs to the *functional unit*, which in this case is only one unit of ``A``. Note that the functional unit can have multiple inputs.

.. code-block:: python

    for node_id, amount in functional_unit:
        edges.append({
            "to": -1,  # Special id of functional unit
            "from": node_id,
            "amount": amount,  # By definition
            "exc_amount": amount,  # By definition
            "impact": LCA(node_id, amount).score,  # Evaluate LCA impact score for this node_id and amount
        })

Finally, we push each node to the **heap**:

.. code-block:: python

    for node_id, amount in functional_unit:
        heappush(heap, (abs(1 / LCA(node_id, amount).score), node_id))

This is not so easy to understand at first glance. What is ``1 / LCA(node_id, amount).score``? Why the absolute value? What is this ``heappush`` thing?

We want one *divided by* the LCA impact score for node ``A`` because our **heap** is sorted in ascending order, and we want the highest score to be first.

We take the absolute value because we are interested in the magnitude of node scores in deciding which node to process next, not the sign of the score - leaving out the absolute value would put all negative scores at the top of the heap (which is sorted in ascending order).

``heappush`` is just a call to push something on to the **heap**, which is our automatically sorted list of nodes to examine.

After this first iteration, we have the following nodes and edges in our graph traversal:

.. image:: images/gt-step-1.png
    :align: center

.. code-block:: python

    nodes = {-1: {'amount': 1, 'cum': some number, 'ind': some small number}}
    edges = [{
        'to': -1,
        'from': 0,  # Assuming A is 0
        'amount': 1,
        'exc_amount': 1,
        'impact': some number
    }]
    heap = [(some number, 0)]

After this is it rather simple: pull off the next node from the *heap*, add it to the list of nodes, construct its edges, and add its inputs to the heap. Iterate until no new nodes are found.

.. image:: images/gt-step-2.png
    :align: center

There are two more things to keep in mind:

* We use a cutoff criteria to stop traversing the supply chain - any node whose cumulative LCA impact score is too small is not added to the heap.
* We only visit each node once. The is functionality in ``bw2analyzer`` to "unroll" the supply chain so that each process can occur more than once.
