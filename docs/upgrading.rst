Upgrading from Version 1
========================

Upgrading from version 1 requires a full export of your data objects, and reimporting them after upgrading the software. Please follow these steps:

1. **Don't** upgrade your software yet! Instead, first export your databases and methods into Brightway packages:

.. code-block:: python

    from bw2data import *
    from bw2data.io import BW2Package

    for index, name in enumerate(databases):
        BW2Package.export_obj(Database(name), "db-{}".format(index), "upgrade")

    for index, name in enumerate(methods):
        BW2Package.export_obj(Method(name), "lcia-{}".format(index), "upgrade")

    # Add in any other objects you want to export here

    # Might have to remove parenthese around print statement
    print("Your exported objects are here:", config.request_dir("upgrade"))

2. Upgrade your software following the installation guide.

3. Each data directory would now be a new project. You can import the objects you exported earlier like this:

.. code-block:: python

    from brightway2 import *
    import os

    preferences['allow incomplete imports'] = True

    filepath = "path that was printed earlier in section 1"
    projects.current = "name of this project"

    for filename in sorted(os.listdir(filepath)):
        print(filename)
        BW2Package.import_file(os.path.join(filepath, filename))

You will need to do this for each data directory you want to upgrade.
