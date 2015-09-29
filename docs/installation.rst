.. _installation:

Installation
************

Brightway2 can be installed pretty much everywhere, on Windows, OS X, Linux, and anywhere else Python can be compiled.

.. note:: Brightway2 supports python 2 and 3, but the recommended version is python 3.4.

.. note:: Please subscribe to the `brightway2 updates mailing list <https://tinyletter.com/brightway2-updates>`__ to be informed of new releases.

Windows
=======

Installation package
--------------------

1. Download the `Brightway2 Windows installation package <brightwaylca.org/data/bw2-python-windows.7z>`__, and extract to the ``C:\`` drive, using something like `7-zip <http://www.7-zip.org/>`__. This will create the directory ``C:\bw2-python\``. If you didn't extract it to the right place, you can always move it afterwards.

.. note:: It is important that the final directory is exactly ``C:\bw2-python\``, as this is what the batch files expect. If you want something more customized, please see the :ref:`advanced-installation` instructions.

2. As Brightway2 is in active development, make sure you have the latest sources by running (double-click) ``C:\bw2-python\bw2-update.bat``.
3. Launch (double-click) the application ``C:\bw2-python\bw2-notebook.bat`` to start a notebook server, or ``C:\bw2-python\bw2-ipython.bat`` to get an IPython shell.

You can safely move these batch files to your desktop for easy access.

Will the installation package mess up other installations of Python?
--------------------------------------------------------------------

No, the installation package is completely independent, and doesn't write anything into your system registry or any other global files.

Launching and using a command shell
-----------------------------------

You can also manually launch Python in a command shell using the application launcher. The launch procedure varies depending on the version of Windows you are running, but is usually next to the main Windows home button. Typing ``cmd`` should be enough to find the program you are looking for:

.. image:: images/cmd-shell-1.png
    :align: center

.. note:: You can usually use the right mouse button to paste into command shell or PowerShell windows.

You can copy and paste, or simply type commands, into the command shell. You will need to run the batch file ``C:\bw2-python\bw2-env.bat`` in each new command shell, to activate the brightway2 environment.

.. image:: images/cmd-shell-2.png
    :align: center

In the command shell, you can enter the ipython interpreter with ``ipython``, or run notebooks with ``jupyter notebook``. Note that you can't launch the notebook server from the ``C:\``, you must be in a directory.

Using PowerShell
----------------

PowerShell is more familiar for some people; in this case, you don't want to run the batch file, but just directly add the relevant directories to your path:

.. code-block:: bat

    $Env:Path = "c:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;" + $Env:Path

You will have to do this in each PowerShell session.

PowerShell scripts are more powerful than normal batch scripts, but have more security features which have defeated my efforts to set the correct path programmatically. You are welcome to fix this!

Creating the installation package
---------------------------------

The installation directory is created by following the advanced installation instructions, adding several batch files, and compressing the python directory.

bw2-env.bat
```````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2

bw2-update.bat
``````````````

.. code-block:: bat

    @ECHO OFF
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    @ECHO ON
    pip install -U --no-deps --pre --extra-index-url http://129.132.92.166:8787/simple/ --trusted-host 129.132.92.166 brightway2
    PAUSE

bw2-ipython.bat
```````````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    CALL ipython

bw2-notebook.bat
````````````````

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    CALL jupyter notebook

Mac OS X
========

Currently, there is no magic installation package for OS X. Please follow the :ref:`advanced-instructions`.

.. 1. Download the `Brightway2 OS X installation package <brightwaylca.org/data/bw2-python-osx.tar.bz2>`__.
.. 2. Open a terminal window in ``Appplications/Utilities/Terminal.app``, and enter the following command:

.. .. code-block:: bash

..     tar -jxf bw2-python-osx.tar.bz2 ~/

.. .. code-block:: bash

..     export PATH="/Users/<your user name>/bw2-python/bin:$PATH"
..     activate bw2

.. 4. In the same terminal window, you can enter the ipython interpreter with the command ``ipython``, or run Jupyter notebooks with ``jupyter notebook``.
