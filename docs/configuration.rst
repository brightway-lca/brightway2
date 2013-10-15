.. _configuration:

Configuration
*************

Get started with the web interface. In a shell or command prompt, type:

.. code-block:: bash

    bw2-web.py

.. image:: images/configuration-1.png
    :align: center

Brightway2 will determine that you are starting it for the first time. You will need to create a :ref:`data-directory` - a writable directory where all data will be stored.

    1. Click to open directories, and navigate to where you want the data directory to be created.
    2. Check to make sure the directory path is correct.
    3. Keep the default name for the data directory - ``brightway2`` - or choose your own.
    4. Click to create and populate the data directory.

.. image:: images/configuration-2.png
    :align: center

.. image:: images/configuration-3.png
    :align: center

Brightway2 comes with some basic metadata - LCIA methods and a biosphere database. They will be automatically downloaded.

.. image:: images/configuration-4.png
    :align: center

Brightway2 is configured and ready!

Configuration through the command line
--------------------------------------

Configuration can also be done with the command line utility ``bw2-controller.py``. First create a data directory somewhere, and note the location. Then run:

.. code-block:: bash

    bw2-controller.py setup --data-dir=/my/created/directory
