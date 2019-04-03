
Testing and Known Issues
************************

Testing
=======

Continuous integration tests are run using `Appveyor <https://www.appveyor.com/>`__ on Windows using Python 2.7 ad 3.5. Developers should also run test locally during development.

Appveyor build status
---------------------

Brightway2-data

.. image:: https://ci.appveyor.com/api/projects/status/uqixaochulbu6vjv?svg=true
   :target: https://ci.appveyor.com/project/cmutel/brightway2-data
   :alt: bw2data build status

Brightway2-calc

.. image:: https://ci.appveyor.com/api/projects/status/uqixaochulbu6vjv?svg=true
   :target: https://ci.appveyor.com/project/cmutel/brightway2-calc
   :alt: bw2calc build status

Brightway2-io

.. image:: https://ci.appveyor.com/api/projects/status/7dox9te430eb2f8h?svg=true
   :target: https://ci.appveyor.com/project/cmutel/brightway2-io
   :alt: bw2io build status

.. _knownissues:

Known Issues
============

brightway2
----------

`brightway2 <http://bitbucket.org/cmutel/brightway2/issues/>`__

Issues
``````

* #18 `ecospold2 import fails: no geography <https://bitbucket.org/cmutel/brightway2/issues/18/ecospold2-import-fails-no-geography>`__
* #19 `Cannot change exchange amount <https://bitbucket.org/cmutel/brightway2/issues/19/cannot-change-exchange-amount>`__
* #20 `pyprind causing problems in various contexts <https://bitbucket.org/cmutel/brightway2/issues/20/pyprind-causing-problems-in-various>`__
* #6 `Replace \`hasattr\` <https://bitbucket.org/cmutel/brightway2/issues/6/replace-hasattr>`__

Enhancements
````````````

* #7 `Conceptual inconsistencies with activities/products and exchanges in ecoinvent <https://bitbucket.org/cmutel/brightway2/issues/7/conceptual-inconsistencies-with-activities>`__

brightway2-analyzer
-------------------

`brightway2-analyzer <http://bitbucket.org/cmutel/brightway2-analyzer/issues/>`__

Issues
``````

* #3 `\`bw2analyzer.recurse_tagged_database\` not compatible with \`presamples\` <https://bitbucket.org/cmutel/brightway2-analyzer/issues/3/bw2analyzerrecurse_tagged_database-not>`__

Enhancements
````````````

* #2 `Make HTML report for an LCA object <https://bitbucket.org/cmutel/brightway2-analyzer/issues/2/make-html-report-for-an-lca-object>`__

brightway2-calc
---------------

`brightway2-calc <http://bitbucket.org/cmutel/brightway2-calc/issues/>`__

Issues
``````

* #15 `Factorization result can be stale <https://bitbucket.org/cmutel/brightway2-calc/issues/15/factorization-result-can-be-stale>`__

Enhancements
````````````

* #14 `All Monte Carlo calculations should support running without access to bw2data <https://bitbucket.org/cmutel/brightway2-calc/issues/14/all-monte-carlo-calculations-should>`__
* #17 `Log and make calculations reproducible <https://bitbucket.org/cmutel/brightway2-calc/issues/17/log-and-make-calculations-reproducible>`__
* #19 `ParameterVectorLCA should make it easy to include parameter values <https://bitbucket.org/cmutel/brightway2-calc/issues/19/parametervectorlca-should-make-it-easy-to>`__
* #20 `ParameterVectorLCA doesn't add presample values to \`sample\` <https://bitbucket.org/cmutel/brightway2-calc/issues/20/parametervectorlca-doesnt-add-presample>`__
* #4 `Create bw2remote and package functionality for offline calculations <https://bitbucket.org/cmutel/brightway2-calc/issues/4/create-bw2remote-and-package-functionality>`__

brightway2-data
---------------

`brightway2-data <http://bitbucket.org/cmutel/brightway2-data/issues/>`__

Issues
``````

* #36 `LCI instead of unit process data imports of 3.2 causes huge CPU/memory issues <https://bitbucket.org/cmutel/brightway2-data/issues/36/lci-instead-of-unit-process-data-imports>`__
* #54 `Use enum for e.g. type dictionary <https://bitbucket.org/cmutel/brightway2-data/issues/54/use-enum-for-eg-type-dictionary>`__
* #55 `Not possible to change unit of input exchanges <https://bitbucket.org/cmutel/brightway2-data/issues/55/not-possible-to-change-unit-of-input>`__

Enhancements
````````````

* #25 `Add utility function to sync database changes across projects <https://bitbucket.org/cmutel/brightway2-data/issues/25/add-utility-function-to-sync-database>`__
* #42 `Set output directory with environment variable <https://bitbucket.org/cmutel/brightway2-data/issues/42/set-output-directory-with-environment>`__
* #46 `bulk update of exchanges is slow with peewee <https://bitbucket.org/cmutel/brightway2-data/issues/46/bulk-update-of-exchanges-is-slow-with>`__
* #49 `Calculation log files - store and parse <https://bitbucket.org/cmutel/brightway2-data/issues/49/calculation-log-files-store-and-parse>`__
* #57 `Give us a convenience method to get exchanges <https://bitbucket.org/cmutel/brightway2-data/issues/57/give-us-a-convenience-method-to-get>`__

brightway2-io
-------------

`brightway2-io <http://bitbucket.org/cmutel/brightway2-io/issues/>`__

Issues
``````

* #19 `ecoinvent 3.1 cutoff has unlinked exchanges in bw2 dev / win 7 /py3 <https://bitbucket.org/cmutel/brightway2-io/issues/19/ecoinvent-31-cutoff-has-unlinked-exchanges>`__
* #38 `Documentation should be more clear on how to remove strategies from default list. <https://bitbucket.org/cmutel/brightway2-io/issues/38/documentation-should-be-more-clear-on-how>`__
* #45 `New parameters approach doesn't work with SimaPro importer <https://bitbucket.org/cmutel/brightway2-io/issues/45/new-parameters-approach-doesnt-work-with>`__
* #47 `US LCI database linking <https://bitbucket.org/cmutel/brightway2-io/issues/47/us-lci-database-linking>`__
* #48 `Missing biosphere flows for consequential 3.2 and 3.3 <https://bitbucket.org/cmutel/brightway2-io/issues/48/missing-biosphere-flows-for-consequential>`__
* #49 `Default strategies shouldn't assume that base data is installed <https://bitbucket.org/cmutel/brightway2-io/issues/49/default-strategies-shouldnt-assume-that>`__
* #50 `Should be easy to recalculate \`amount\` field based on parameters in importers <https://bitbucket.org/cmutel/brightway2-io/issues/50/should-be-easy-to-recalculate-amount-field>`__
* #52 `Cannot import ELCD3.2 database. <https://bitbucket.org/cmutel/brightway2-io/issues/52/cannot-import-elcd32-database>`__
* #57 `Strip Pathlib instances to make them JSON serializable <https://bitbucket.org/cmutel/brightway2-io/issues/57/strip-pathlib-instances-to-make-them-json>`__
* #58 `Issue importing any version of ecoinvent 3 on my machine <https://bitbucket.org/cmutel/brightway2-io/issues/58/issue-importing-any-version-of-ecoinvent-3>`__

Enhancements
````````````

* #10 `Need ecoinvent 3.01 -> 3.1 migration <https://bitbucket.org/cmutel/brightway2-io/issues/10/need-ecoinvent-301-31-migration>`__
* #11 `Need ecoinvent 3.1 -> 3.2 migration <https://bitbucket.org/cmutel/brightway2-io/issues/11/need-ecoinvent-31-32-migration>`__
* #12 `Comparison chart for each major/freely available database <https://bitbucket.org/cmutel/brightway2-io/issues/12/comparison-chart-for-each-major-freely>`__
* #13 `SimaPro LCIA importer: Waste types seem to be handled incorrectly <https://bitbucket.org/cmutel/brightway2-io/issues/13/simapro-lcia-importer-waste-types-seem-to>`__
* #14 `Need clever approach to replace formula parameters names that conflict with Python reserved words <https://bitbucket.org/cmutel/brightway2-io/issues/14/need-clever-approach-to-replace-formula>`__
* #15 `Importer for OLCA JSON LD schema <https://bitbucket.org/cmutel/brightway2-io/issues/15/importer-for-olca-json-ld-schema>`__
* #26 `Need SimaPro migration for ecoinvent 3.2 names <https://bitbucket.org/cmutel/brightway2-io/issues/26/need-simapro-migration-for-ecoinvent-32>`__
* #27 `Rework uncertainty with pedigree matrices <https://bitbucket.org/cmutel/brightway2-io/issues/27/rework-uncertainty-with-pedigree-matrices>`__
* #29 `biosphere consistency check (for bw2_setup()) <https://bitbucket.org/cmutel/brightway2-io/issues/29/biosphere-consistency-check-for-bw2_setup>`__
* #34 `Migrations need to be cleaned up <https://bitbucket.org/cmutel/brightway2-io/issues/34/migrations-need-to-be-cleaned-up>`__
* #46 `Handling of imported parameter with both \`value\` and \`formula\` <https://bitbucket.org/cmutel/brightway2-io/issues/46/handling-of-imported-parameter-with-both>`__
* #7 `SimaPro CSV should extract and apply unit conversions when possible <https://bitbucket.org/cmutel/brightway2-io/issues/7/simapro-csv-should-extract-and-apply-unit>`__
* #8 `Need SimaPro to ecoinvent biosphere migration <https://bitbucket.org/cmutel/brightway2-io/issues/8/need-simapro-to-ecoinvent-biosphere>`__
* #9 `Need ecoinvent 2.2 -> 3.01 migration <https://bitbucket.org/cmutel/brightway2-io/issues/9/need-ecoinvent-22-301-migration>`__

brightway2-parameters
---------------------

`brightway2-parameters <http://bitbucket.org/cmutel/brightway2-parameters/issues/>`__

Issues
``````

* #3 `Global params can be Numpy arrays <https://bitbucket.org/cmutel/brightway2-parameters/issues/3/global-params-can-be-numpy-arrays>`__

brightway2-regional
-------------------

`brightway2-regional <http://bitbucket.org/cmutel/brightway2-regional/issues/>`__

Enhancements
````````````

* #3 `Mark databases as regionalized <https://bitbucket.org/cmutel/brightway2-regional/issues/3/mark-databases-as-regionalized>`__

brightway2-restapi
------------------

`brightway2-restapi <http://bitbucket.org/cmutel/brightway2-restapi/issues/>`__

Enhancements
````````````

* #4 `With the DELETEs, i would return a 204 - no content. <https://bitbucket.org/cmutel/brightway2-restapi/issues/4/with-the-deletes-i-would-return-a-204-no>`__

brightway2-temporalis
---------------------

`brightway2-temporalis <http://bitbucket.org/cmutel/brightway2-temporalis/issues/>`__

Issues
``````

* #4 `Traversal in a graph with a loop never ends <https://bitbucket.org/cmutel/brightway2-temporalis/issues/4/traversal-in-a-graph-with-a-loop-never>`__

Enhancements
````````````

* #2 `make possible to redo dynamic LCA for same db without redoing LCI <https://bitbucket.org/cmutel/brightway2-temporalis/issues/2/make-possible-to-redo-dynamic-lca-for-same>`__

