.. _quick-windows-install:

Windows Installation Package
****************************

The installation package is a single directory

1. Download the `Brightway2 Windows installation package <https://brightwaylca.org/data/bw2-python-windows.7z>`__, and extract to the ``C:\`` drive, using something like `7-zip <http://www.7-zip.org/>`__. This will create the directory ``C:\bw2-python\``. If you didn't extract it to the right place, you can always move it afterwards.

.. note:: It is important that the final directory is exactly ``C:\bw2-python\``, as this is what the batch files expect. If you want something more customized, please see the :ref:`advanced-installation` instructions.

2. As Brightway2 is in active development, make sure you have the latest sources by running (double-click) ``C:\bw2-python\bw2-update.bat``.

3. Launch (double-click) the application ``C:\bw2-python\bw2-notebook.bat`` to start a notebook server, or ``C:\bw2-python\bw2-ipython.bat`` to get an IPython shell.

You can safely copy or move these batch files to your desktop for easy access.

Will the installation package mess up other installations of Python?
--------------------------------------------------------------------

No, the installation package is completely independent directory, and doesn't write anything into your system registry or any other global variables.

Launching and using a command shell
-----------------------------------

You can also manually launch Python in a command shell using the application launcher. The launch procedure varies depending on the version of Windows you are running, but is usually next to the main Windows home button. Typing ``cmd`` should be enough to find the program you are looking for:

.. image:: images/cmd-shell-1.png
    :align: center

.. note:: You can usually use the right mouse button to paste into command shell or PowerShell windows.

You can copy and paste, or simply type commands, into the command shell. You will need to run the batch file ``C:\bw2-python\bw2-env.bat`` in each new command shell, to activate the brightway2 environment.

.. image:: images/cmd-shell-2.png
    :align: center

In the command shell, you can enter the ipython interpreter with ``ipython``, or run notebooks with ``jupyter notebook``. Note that you can't launch the notebook server from the root ``C:\`` drive, you must be in a directory, e.g. ``C:\my-notebooks\``.

Using PowerShell
----------------

PowerShell is more familiar for some people; in this case, you don't want to run the batch file, but just directly add the relevant directories to your path:

.. code-block:: bat

    $Env:Path = "c:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;" + $Env:Path

You will have to do this in each PowerShell session.

PowerShell scripts are more powerful than normal batch scripts, but have more security features which have defeated my efforts to set the correct path programmatically. You are welcome to fix this!

.. _windows-scripts:

Scripts in the installation package
-----------------------------------

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
    pip install -U --no-deps --pre brightway2 bw2io bw2data bw2calc bw2analyzer
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

bw2-activity-browser.bat
````````````````````````

.. note:: The activity browser is still under heavy development. Use with caution!

.. code-block:: bat

    @ECHO OFF
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2
    @ECHO ON
    CALL activity-browser.exe
    PAUSE

Notebook directory
==================

It is best practice to store your notebooks in a different directory outside of the ``bw2-python`` directory - and probably separate directories for each project you are working on. One reasonable place would be in your ``Documents`` or ``Desktop``. You can safely copy the notebooks script to this other directory (or directories).
