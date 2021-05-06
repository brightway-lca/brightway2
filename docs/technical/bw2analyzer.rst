Brightway2-analyzer
*******************

Contribution analysis
=====================

.. autoclass:: bw2analyzer.contribution.ContributionAnalysis
    :members:

Supply chain traversal
======================

.. autofunction:: bw2analyzer.traverse_tagged_databases

This function uses the following help functions:

.. autofunction:: bw2analyzer.tagged.aggregate_tagged_graph

.. autofunction:: bw2analyzer.tagged.recurse_tagged_database

LCA reports
===========

.. autoclass:: bw2analyzer.report.SerializedLCAReport
    :members:

PageRank algorithm
==================

.. autoclass:: bw2analyzer.page_rank.PageRank
    :members:

Comparison functions
====================

.. autofunction:: bw2analyzer.comparisons.compare_activities_by_grouped_leaves

.. autofunction:: bw2analyzer.utils.print_recursive_calculation

.. autofunction:: bw2analyzer.utils.print_recursive_supply_chain

.. autofunction:: bw2analyzer.comparisons.find_differences_in_inputs

.. autofunction:: bw2analyzer.comparisons.compare_activities_by_lcia_score
