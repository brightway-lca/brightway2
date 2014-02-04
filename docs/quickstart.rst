Windows quickstart
******************

This is the easiest way to get started using Brightway2 on **Windows**. If you are interested in other installation options, or are using **Mac OS X** or **Linux**, see the other installation options:

* :ref:`windows-install`
* :ref:`os-x-install`
* :ref:`linux-install`

Installing Python
-----------------

The easiest way to install Brightway2 is to use `Enthought Canopy <https://www.enthought.com/products/canopy/>`_, which is a full Python distribution. It is free for academics. See the installation documentation for other options.

.. warning:: `Canopy Express <https://www.enthought.com/canopy-express/>`_ will not work with Brightway2, as it does `not include the lxml package <https://enthought.com/products/canopy/package-index/>`_.

After installing Canopy and all Canopy packages, install the free package ``pip``. You can then install Brightway2 in the ipython shell in the editor:

.. code-block:: bash

    !pip install brightway2

.. image:: images/canopy-console-ipython.png
    :align: center

Running Brightway2
------------------

Finally, in a command prompt, start Brightway2:

.. code-block:: bash

    bw2-web.py

This should start the program, and open a new web browser tab to the correct address. Brightway2 will recognize that you are starting it for the first time, and give you instructions on how to download basic data, import your projects, and start working.

.. note:: See also :ref:`configuration`
