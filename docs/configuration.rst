.. _configuration:

Configuration
=============

Configuring Brightway2 is pretty easy - the only thing to do is to tell Brightway2 the location of a directory where it can store data, logs, and exported files. We call this directory the "data directory", and its structure is explained in detail below. The first thing Brightway2 needs is to know where it can save data and log files.

Configuration through the web interface
---------------------------------------

In a terminal shell or command prompt, type:

.. code-block:: bash

    bw2-web

.. image:: images/configuration-1.png
    :align: center

Brightway2 will determine that you are starting it for the first time. You will create a :ref:`data directory <data-directory>` - a writable directory where all data will be stored.

    1. Click to open directories, and navigate to where you want the data directory to be created.
    2. Check to make sure the directory path is correct.
    3. Keep the default name for the new data directory - ``brightway2`` - or choose your own. This directory will be created, it can't already exist.
    4. Click "Set Brightway2 data path" to create and populate the data directory.

.. image:: images/configuration-2.png
    :align: center

.. image:: images/configuration-3.png
    :align: center

Brightway2 comes with some basic metadata - LCIA methods and a biosphere database. They will be automatically downloaded.

.. image:: images/configuration-4.png
    :align: center

Configuration through the command line
--------------------------------------

Configuration can also be done with the command line utility ``bw2-controller``. Simply run the following command, and confirm that you want to create the data directory. The data directory will be created - it shouldn't exist yet.

.. code-block:: bash

    bw2-controller setup --data-dir=/my/new/directory/path

Configuration in a python shell
-------------------------------

The data directory can be set in the python shell, either permanently:

.. code-block:: python

    from brightway2 import set_data_dir
    set_data_dir("/path/to/directory")

or just for the current python session (useful if you have different data directories for each project):

.. code-block:: python

    from brightway2 import set_data_dir
    set_data_dir("/path/to/directory", permanent=False)
