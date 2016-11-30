
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

* #6 `Replace \`hasattr\` <https://bitbucket.org/cmutel/brightway2/issues/6/replace-hasattr>`__

Enhancements
````````````

* #7 `Conceptual inconsistencies with activities/products and exchanges in ecoinvent <https://bitbucket.org/cmutel/brightway2/issues/7/conceptual-inconsistencies-with-activities>`__

brightway2-calc
---------------

`brightway2-calc <http://bitbucket.org/cmutel/brightway2-calc/issues/>`__

Issues
``````

* #15 `Factorization result can be stale <https://bitbucket.org/cmutel/brightway2-calc/issues/15/factorization-result-can-be-stale>`__

Enhancements
````````````

* #11 `Package scikit-umfpack for Windows (Py3.5 only) <https://bitbucket.org/cmutel/brightway2-calc/issues/11/package-scikit-umfpack-for-windows-py35>`__
* #14 `All Monte Carlo calculations should support running without access to bw2data <https://bitbucket.org/cmutel/brightway2-calc/issues/14/all-monte-carlo-calculations-should>`__
* #4 `Create bw2remote and package functionality for offline calculations <https://bitbucket.org/cmutel/brightway2-calc/issues/4/create-bw2remote-and-package-functionality>`__

brightway2-data
---------------

`brightway2-data <http://bitbucket.org/cmutel/brightway2-data/issues/>`__

Issues
``````

* #35 `location filter uses lowercase only and ignores locations with dashes <https://bitbucket.org/cmutel/brightway2-data/issues/35/location-filter-uses-lowercase-only-and>`__
* #36 `LCI instead of unit process data imports of 3.2 causes huge CPU/memory issues <https://bitbucket.org/cmutel/brightway2-data/issues/36/lci-instead-of-unit-process-data-imports>`__
* #43 `All projects default to read-only, enable_writes is powerless <https://bitbucket.org/cmutel/brightway2-data/issues/43/all-projects-default-to-read-only>`__

Enhancements
````````````

* #25 `Add utility function to sync database changes across projects <https://bitbucket.org/cmutel/brightway2-data/issues/25/add-utility-function-to-sync-database>`__
* #29 `Switch from JSON serialized dictionaries to SQLite for metadata wherever possible <https://bitbucket.org/cmutel/brightway2-data/issues/29/switch-from-json-serialized-dictionaries>`__
* #42 `Set output directory with environment variable <https://bitbucket.org/cmutel/brightway2-data/issues/42/set-output-directory-with-environment>`__
* #46 `bulk update of exchanges is slow with peewee <https://bitbucket.org/cmutel/brightway2-data/issues/46/bulk-update-of-exchanges-is-slow-with>`__

brightway2-io
-------------

`brightway2-io <http://bitbucket.org/cmutel/brightway2-io/issues/>`__

Issues
``````

* #1 `BW2Package _create_obj fails sometimes <https://bitbucket.org/cmutel/brightway2-io/issues/1/bw2package-_create_obj-fails-sometimes>`__
* #19 `ecoinvent 3.1 cutoff has unlinked exchanges in bw2 dev / win 7 /py3 <https://bitbucket.org/cmutel/brightway2-io/issues/19/ecoinvent-31-cutoff-has-unlinked-exchanges>`__

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
* #7 `SimaPro CSV should extract and apply unit conversions when possible <https://bitbucket.org/cmutel/brightway2-io/issues/7/simapro-csv-should-extract-and-apply-unit>`__
* #8 `Need SimaPro to ecoinvent biosphere migration <https://bitbucket.org/cmutel/brightway2-io/issues/8/need-simapro-to-ecoinvent-biosphere>`__
* #9 `Need ecoinvent 2.2 -> 3.01 migration <https://bitbucket.org/cmutel/brightway2-io/issues/9/need-ecoinvent-22-301-migration>`__

brightway2-parameters
---------------------

`brightway2-parameters <http://bitbucket.org/cmutel/brightway2-parameters/issues/>`__

Enhancements
````````````

* #2 `Integrate with Monte Carlo random sampling <https://bitbucket.org/cmutel/brightway2-parameters/issues/2/integrate-with-monte-carlo-random-sampling>`__

brightway2-regional
-------------------

`brightway2-regional <http://bitbucket.org/cmutel/brightway2-regional/issues/>`__

Issues
``````

* #1 `display_ia_map changes on multiple executions <https://bitbucket.org/cmutel/brightway2-regional/issues/1/display_ia_map-changes-on-multiple>`__

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

* #3 `dynamic LCA skip incomprehensibly some years <https://bitbucket.org/cmutel/brightway2-temporalis/issues/3/dynamic-lca-skip-incomprehensibly-some>`__

Enhancements
````````````

* #2 `make possible to redo dynamic LCA for same db without redoing LCI <https://bitbucket.org/cmutel/brightway2-temporalis/issues/2/make-possible-to-redo-dynamic-lca-for-same>`__

brightway2-ui
-------------

`brightway2-ui <http://bitbucket.org/cmutel/brightway2-ui/issues/>`__

Enhancements
````````````

* #3 `Massively improve treemap <https://bitbucket.org/cmutel/brightway2-ui/issues/3/massively-improve-treemap>`__
* #4 `Explore new visualization libraries <https://bitbucket.org/cmutel/brightway2-ui/issues/4/explore-new-visualization-libraries>`__
* #7 `Project concept only available in 2.0 branch <https://bitbucket.org/cmutel/brightway2-ui/issues/7/project-concept-only-available-in-20>`__

