Brightway2-calc
***************

.. _matrixbuilders:

Matrix builders
===============

One of the most basic and most important components of ``bw2calc`` is the ability to build a sparse matrix from a processed parameter array.

Matrix Builder
--------------

.. autoclass:: bw2calc.MatrixBuilder
    :members:

Technosphere Biosphere Matrix Builder
-------------------------------------

.. autoclass:: bw2calc.TechnosphereBiosphereMatrixBuilder
    :members:

Indexing
--------

.. autofunction:: bw2calc.indexing.index_with_arrays

.. autofunction:: bw2calc.indexing.index_with_searchsorted

.. _lca:

Static life cycle assessment
============================

.. autoclass:: bw2calc.LCA
    :members:

.. autoclass:: bw2calc.least_squares.LeastSquaresLCA
    :members:

Graph Traversal
===============

.. autoclass:: bw2calc.GraphTraversal
    :members:

.. _montecarlo:

Stochastic Life Cycle Assessment
================================

Monte Carlo LCA
---------------

.. autoclass:: bw2calc.MonteCarloLCA
    :members:

Vector Monte Carlo LCA
----------------------

.. autoclass:: bw2calc.ParameterVectorLCA
    :members:

Parallel Monte Carlo LCA
------------------------

.. autoclass:: bw2calc.ParallelMonteCarlo
    :members:

Utilities
=========

.. autofunction:: bw2calc.utils.load_arrays
