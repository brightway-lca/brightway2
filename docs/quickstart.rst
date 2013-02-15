Windows quickstart
******************

This is the easiest way to get started using Brightway2 on **Windows**. If you are interested in using the full power of the Brightway2 framework, or are using **Mac OS X** or **Linux**, see other installation options:

* :ref:`windows-install`
* :ref:`os-x-install`
* :ref:`linux-install`

First, download the latest version of `Python (x,y) <https://code.google.com/p/pythonxy/wiki/Downloads>`_, and install it. This is the easiest way to get the `NumPy <http://numpy.scipy.org/>`_ and `SciPy <http://scipy.org/>`_ libraries.

* `Python (x,y) <https://code.google.com/p/pythonxy/wiki/Downloads>`_

.. note:: Be sure to check the option to install **pip**:

.. image:: images/python-xy-pip.png
    :align: center

Second, download and install the XML processing library `lxml <http://pythonxy.googlecode.com/files/lxml-3.0.1-1_py27.exe>`_.

* `lxml <http://pythonxy.googlecode.com/files/lxml-3.0.1-1_py27.exe>`_

Third, open a command prompt (Start -> Command Prompt), and type in the following:

.. code-block:: bash

    pip install brightway2

Finally, again in the command prompt, start Brightway2:

.. code-block:: bash

    bw2-web.py

This should start the program, and open a new web browser tab to the correct address. Brightway2 will recognize that you are starting it for the first time, and give you instructions on how to download basic data, import your projects, and start working.
