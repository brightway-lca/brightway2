Brightway2-io
*************

BW2Package
==========

Brightway2 has its own data format for archiving data which is both efficient and compatible across operating systems and programming languages. This is the default backup format for Brightway2 :ref:`datastore` objects.

.. note:: **imports** and **exports** are supported.

.. autoclass:: bw2io.package.BW2Package
    :members:

Migrations
==========

.. autoclass:: bw2io.migrations.Migration
    :members:

.. autofunction:: bw2io.migrations.create_core_migrations

Extractors
==========

Ecospold 1
``````````

.. autoclass:: bw2io.extractors.ecospold1.Ecospold1DataExtractor
    :members:

.. autoclass:: bw2io.extractors.ecospold1_lcia.Ecospold1LCIAExtractor
    :members:

Ecospold 2
``````````

.. autoclass:: bw2io.extractors.ecospold2.Ecospold2DataExtractor
    :members:

Simapro CSV
```````````

.. autoclass:: bw2io.extractors.simapro_csv.SimaProCSVExtractor
    :members:

.. autoclass:: bw2io.extractors.simapro_lcia_csv.SimaProLCIACSVExtractor
    :members:

Importers
=========

Base
````

.. autoclass:: bw2io.importers.base.ImportBase
    :members:

.. autoclass:: bw2io.importers.base_lci.LCIImporter
    :members:

.. autoclass:: bw2io.importers.base_lcia.LCIAImporter
    :members:

Ecospold 1
``````````

Ecospold version 1 is the data format of ecoinvent versions 1 and 2, and the US LCI. It is an XML data format with reasonable defaults.

.. note:: only **imports** are supported.

.. autoclass:: bw2io.importers.ecospold1.SingleOutputEcospold1Importer
    :members:

.. autoclass:: bw2io.importers.ecospold1.MultiOutputEcospold1Importer
    :members:

.. autoclass:: bw2io.importers.ecospold1_lcia.Ecospold1LCIAImporter
    :members:

Ecospold 2
``````````

Ecospold version 2 is the data format of ecoinvent version 3.

.. note:: only **imports** are supported.

.. autoclass:: bw2io.importers.ecospold2.SingleOutputEcospold2Importer
    :members:

.. autoclass:: bw2io.importers.ecospold2_biosphere.Ecospold2BiosphereImporter
    :members:

Ecoinvent
`````````

.. autoclass:: bw2io.importers.ecoinvent_lcia.EcoinventLCIAImporter
    :members:

Simapro
```````

Import a `SimaPro <http://www.pre-sustainability.com/simapro-lca-software>`_ text file.

.. note:: only **imports** are supported.

.. autoclass:: bw2io.importers.simapro_csv.SimaProCSVImporter
    :members:

.. autoclass:: bw2io.importers.simapro_lcia_csv.SimaProLCIACSVImporter
    :members:

Excel
`````

Import an inventory in an Excel spreadsheet which follows the generic `Excel example <https://bitbucket.org/cmutel/brightway2-io/raw/default/bw2io/data/examples/example.xlsx>`__.

.. note:: both imports and exports are supported.

.. autoclass:: bw2io.importers.excel.ExcelImporter

CSV
```

Import an inventory in a CSV file which follows the generic `CSV example <https://bitbucket.org/cmutel/brightway2-io/raw/default/bw2io/data/examples/example.csv>`__.

.. note:: both imports and exports are supported.

.. autoclass:: bw2io.importers.csv.CSVImporter
    :members:

Strategies
==========

Migrations
``````````

.. autofunction:: bw2io.strategies.migrations.migrate_datasets

.. autofunction:: bw2io.strategies.migrations.migrate_exchanges

Generic
```````

.. autofunction:: bw2io.strategies.generic.link_iterable_by_fields

.. autofunction:: bw2io.strategies.generic.assign_only_product_as_production

.. autofunction:: bw2io.strategies.generic.link_technosphere_by_activity_hash

.. autofunction:: bw2io.strategies.generic.set_code_by_activity_hash

.. autofunction:: bw2io.strategies.generic.set_code_by_activity_hash

.. autofunction:: bw2io.strategies.generic.tupleize_categories

.. autofunction:: bw2io.strategies.generic.drop_unlinked

.. autofunction:: bw2io.strategies.generic.normalize_units

Biosphere
`````````

.. autofunction:: bw2io.strategies.biosphere.drop_unspecified_subcategories

.. autofunction:: bw2io.strategies.biosphere.normalize_biosphere_names

.. autofunction:: bw2io.strategies.biosphere.normalize_biosphere_categories

.. autofunction:: bw2io.strategies.biosphere.strip_biosphere_exc_locations

LCIA
````

.. autofunction:: bw2io.strategies.lcia.add_activity_hash_code

.. autofunction:: bw2io.strategies.lcia.drop_unlinked_cfs

.. autofunction:: bw2io.strategies.lcia.set_biosphere_type

.. autofunction:: bw2io.strategies.lcia.match_subcategories

Ecospold 1
``````````

.. autofunction:: bw2io.strategies.ecospold1_allocation.clean_integer_codes

.. autofunction:: bw2io.strategies.ecospold1_allocation.es1_allocate_multioutput

.. autofunction:: bw2io.strategies.ecospold1_allocation.allocate_exchanges

Ecospold 2
``````````

.. autofunction:: bw2io.strategies.ecospold2.link_biosphere_by_flow_uuid

.. autofunction:: bw2io.strategies.ecospold2.remove_zero_amount_coproducts

.. autofunction:: bw2io.strategies.ecospold2.remove_zero_amount_inputs_with_no_activity

.. autofunction:: bw2io.strategies.ecospold2.es2_assign_only_product_with_amount_as_reference_product

.. autofunction:: bw2io.strategies.ecospold2.assign_single_product_as_activity

.. autofunction:: bw2io.strategies.ecospold2.create_composite_code

.. autofunction:: bw2io.strategies.ecospold2.link_internal_technosphere_by_composite_code

.. autofunction:: bw2io.strategies.ecospold2.delete_exchanges_missing_activity

.. autofunction:: bw2io.strategies.ecospold2.delete_ghost_exchanges

Simapro
```````

.. autofunction:: bw2io.strategies.simapro.sp_allocate_products

.. autofunction:: bw2io.strategies.simapro.link_technosphere_based_on_name_unit_location

.. autofunction:: bw2io.strategies.simapro.split_simapro_name_geo

.. autofunction:: bw2io.strategies.simapro.normalize_simapro_biosphere_categories

.. autofunction:: bw2io.strategies.simapro.normalize_simapro_biosphere_names

.. autofunction:: bw2io.strategies.simapro.normalize_simapro_formulae

Special
```````

.. autofunction:: bw2io.strategies.special.add_dummy_processes_and_rename_exchanges

Export
======

.. autofunction:: bw2io.export.excel.write_lci_excel

.. autofunction:: bw2io.export.csv.write_lci_csv

.. autofunction:: bw2io.export.excel.lci_matrices_to_excel

.. autofunction:: bw2io.export.excel.write_lci_activities

.. autofunction:: bw2io.export.excel.write_lci_matching

.. autofunction:: bw2io.export.excel.write_lcia_matching

`Gephi <http://gephi.org/>`_ is an open-source graph visualization and analysis program.

.. note:: only **exports** are supported.

.. autoclass:: bw2io.export.gexf.DatabaseToGEXF
    :members:

.. autofunction:: bw2io.export.matlab.lci_matrices_to_matlab

.. _backup-data-directory:

Backups
=======

.. autofunction:: bw2io.backup.backup_data_directory

.. autofunction:: bw2io.backup.backup_project_directory

Data
====

.. autofunction:: bw2io.data.write_json_file

.. autofunction:: bw2io.data.get_ecoinvent_301_31_migration_data

.. autofunction:: bw2io.data.get_ecoinvent_2_301_migration_data

.. autofunction:: bw2io.data.get_biosphere_2_3_category_migration_data

.. autofunction:: bw2io.data.get_biosphere_2_3_name_migration_data

.. autofunction:: bw2io.data.get_us_lci_migration_data

.. autofunction:: bw2io.data.convert_simapro_ecoinvent_elementary_flows

.. autofunction:: bw2io.data.get_simapro_ecoinvent_3_migration_data

.. autofunction:: bw2io.data.convert_ecoinvent_2_301

.. autofunction:: bw2io.data.convert_lcia_methods_data
