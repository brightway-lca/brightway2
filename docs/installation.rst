.. _installation:

Installation
************

Brightway2 can be installed pretty much everywhere, on Windows, OS X, Linux, and anywhere else Python can be compiled.

.. note:: Brightway2 supports python 2 and 3, but the recommended version is python 3.4.

.. note:: Please subscribe to the `brightway2 updates mailing list <https://tinyletter.com/brightway2-updates>`__ to be informed of new releases.

Windows
=======

1. Download the `Brightway2 Windows installation package <brightwaylca.org/data/bw2-python-windows.7z>`__.
2. Next, use something like `7-zip <http://www.7-zip.org/>`__ to decompress this file to the ``C:`` drive, creating the directory ``C:\bw2-python``.
3. In a command shell, run the following program: ``C:\bw2-python\bw2-env.bat``.

.. warning:: You will need to run this small program every time you open a new command shell window.

4. In the same command shell, you can enter the ipython interpreter with ``ipython``, or run notebooks with ``jupyter notebook``. Note that you can't launch the notebook server from the ``C:\``, you must be in a directory.

Launching and using a command shell
-----------------------------------

Launch a command shell using the application launcher. This varies depending on the version of Windows you are running, but is usually next to the main Windows home button. Typing ``cmd`` should be enough to find the program you are looking for:

.. image:: images/cmd-shell-1.png
    :align: center

.. note:: You can usually use the right mouse button to paste into command shell or PowerShell windows.

It should be as simple as copying and pasting the commands from #3 and #4:

.. image:: images/cmd-shell-2.png
    :align: center

Using PowerShell
----------------

PowerShell is more familiar for some people; in this case, you don't want to run the batch file, but just directly add the relevant directories to your:

.. code-block:: bat

    $Env:Path = "c:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;" + $Env:Path

PowerShell scripts are more powerful than normal batch scripts, but have more security features which have defeated my efforts to set the correct path programmatically. You are welcome to fix this!

Installing in a different location
----------------------------------

Installing in a different location is fine - it shouldn't break anything - but you will have to adjust the paths in ``bw2-env.bat`` (or the PowerShell command above) to match the directory you have chosen.

What is in the installation package?
------------------------------------

This is a directory created using the `Continuum Miniconda` installer. After installation, an environment called ``bw2`` was created, and all packages necessary for Brightway2 were installed. Finally, the ``bw2-env.bat`` file was created. It is quite simple:

.. code-block:: bat

    @ECHO OFF
    ECHO Setting path to Brightway2 environment
    set PATH=C:\bw2-python\envs\bw2\Scripts\;C:\bw2-python\Scripts\;C:\bw2-python\;%PATH%
    CALL C:\bw2-python\Scripts\activate.bat bw2

Will the installation package mess up other installations of Python?
--------------------------------------------------------------------

No, the installation package is completely independent, and doesn't write anything into your system registry or any other global files.

Mac OS X
========

1. Download the `Brightway2 OS X installation package <brightwaylca.org/data/bw2-python-osx.tar.bz2>`__.
2. Open a terminal window in ``Appplications/Utilities/Terminal.app``, and enter the following command:

.. code-block:: bash

    tar -jxf bw2-python-osx.tar.bz2 ~/

.. code-block:: bash

    export PATH="/Users/<your user name>/bw2-python/bin:$PATH"
    activate bw2

4. In the same terminal window, you can enter the ipython interpreter with the command ``ipython``, or run Jupyter notebooks with ``jupyter notebook``.
