.. _installation:

Installation
************

Brightway2 can be installed pretty much everywhere, on Windows, OS X, Linux, and anywhere else Python can be compiled.

.. note:: Brightway2 supports python 2 and 3, but the recommended version is python 3.4.

.. note:: Please subscribe to the `brightway2 updates mailing list <https://tinyletter.com/brightway2-updates>`__ to be informed of new releases.

.. warning:: These instructions are for the development version of Brightway2 - some things might not work as intended! Please email cmutel@gmail.com with bug reports or frustrated desires.

.. _anaconda:

Recommended installation: Continuum Miniconda
=============================================

1. Save `Miniconda 3.4 (64-bit version) <http://conda.pydata.org/miniconda.html>`__ for your OS

On Mac OS X, you might have to make the bash shell executable:

.. code-block:: bash

    chmod +x ~/Downloads/Miniconda3-latest-MacOSX-x86_64.sh

(or whatever version you have; you should probably adjust the path as well)

2. Run the Miniconda installer. Make it your default python.

3. In a terminal window or command prompt, make sure ``conda`` is up to date:

.. code-block:: bash

    conda install conda
    conda update conda

4. Create a python environ for brightway2:

.. code-block:: bash

    conda create -n bw2 anaconda python=3.4

5. Activate your environment:

.. code-block:: bash

    activate bw2

You will have to activate your brightway2 environment in each new terminal window or command prompt.

6. Install some dependencies:

.. code-block:: bash

   conda install numpy ipython ipython-notebook scipy flask lxml requests pip nose future docopt whoosh

6a. If you are on Windows, you also need to do:

.. code-block:: bash

    conda install pywin32

7. Install some more dependencies:

.. code-block:: bash

    pip install pyprind unicodecsv voluptuous bw2speedups

8. Finally, install the development version of brightway2:

.. code-block:: bash

   pip install --pre --extra-index-url http://129.132.92.166:8787/simple/ --trusted-host 129.132.92.166 brightway2

You can now use brightway2 from the python shell or in an ipython notebook.

.. _windows-install:

Alternatives
============

Windows
-------

Although Brightway2 is relatively simple, installation of the numerical and scientific libraries can be difficult as there is no default compilers installed on most Windows machines. This issue is well-known in the Python community (see `Pycon keynote <https://www.youtube.com/watch?v=d1a4Jbjc-vU>`_, recent `reddit discussion <http://www.reddit.com/r/Python/comments/2bbd5t/stop_struggling_with_python_on_windows/>`_). The only sensible way is to use a precompiled set of packages.

In addition to ``conda``, the following also work well, but no specific instructions are provided:

.. _canopy:

Enthought Canopy
````````````````

.. warning:: `Canopy Express <https://www.enthought.com/canopy-express/>`_ will not work with Brightway2, as it does `not include the lxml package <https://enthought.com/products/canopy/package-index/>`_.

`Enthought Canopy <https://www.enthought.com/products/canopy/>`_ provides a nice Python environment and free academic licenses.


Python(x,y)
```````````

Download and install the `Python(x,y) executable <https://code.google.com/p/pythonxy/wiki/Downloads>`_. All the necessary background libraries will be installed.

Winpython
`````````

`Winpython <http://winpython.sourceforge.net/>`_ is another set of Windows Python packages, similar to Python(x,y). I haven't tried this, but have heard good things. I think you will have to use either ``easy_install`` or `Christoph Gohlke's Windows binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ to install lxml.

.. _os-x-install:

Max OS X
--------

On OS X, there are almost too many choices that work well. The simplest way is to use :ref:`canopy` or :ref:`anaconda` - the instructions are the same as on Windows. Alternatively, there are two main OS X-specific alternatives for installing Python packages: `Macports <http://www.macports.org/>`_ and `Homebrew <http://mxcl.github.com/homebrew/>`_. Brightway2 is developed primarily on OS X using Macports, but as it depends on a few standard libraries, either alternative should work well. Homebrew users will have to adapt the following instructions, but reports are that this is relatively simple.

.. note:: See also the :ref:`developer-os-x` notes for an even more powerful & complicated approach, good for software developers.

Follow the `instructions <http://www.macports.org/install.php>`_ and install Macports. Note that both Macports and Homebrew require Xcode to be installed first. Xcode can be installed from the OS X installation disk (for 10.6 or lower), the app store (10.7 or higher), or `other unofficial sources <https://github.com/kennethreitz/osx-gcc-installer>`_.

Next, install the needed Python libraries using this command in the Terminal:

.. code-block:: bash

	sudo port install python_select py34-scipy py34-numpy py34-pip py34-libxml2 py34-nose py34-sphinx py34-requests py34-flask

Point to the correct Python executable:

.. code-block:: bash

    sudo port select --set python python34

Next, install the Brightway2 source code using another Terminal command:

.. code-block:: bash

	pip-3.4 install --user brightway2

Unfortunately, the Brightway2 scripts aren't in our ``PATH`` environment variable yet. Fix this by adding the following line to the end of the ``.profile`` file in your home directory, and then start a new terminal window:

.. code-block:: bash

    export PATH=$PATH:/opt/local/Library/Frameworks/Python.framework/Versions/3.4/bin

.. _linux-install:

Linux
-----

General instructions are provided for Ubuntu; people using other distributions are assumed smart to be enough to adapt as necessary. See also :ref:`platform-agnostic` instructions above.

First, install the required ``apt`` packages. You can select them in the graphical interface, or through one command in the terminal:

.. code-block:: bash

	sudo apt-get install python-scipy python-numpy python-nose python-pip python-libxml2 python-sphinx python-virtualenv python-virtualenvwrapper

Next, install Brightway2 using another terminal command:

.. code-block:: bash

	pip install --user brightway2

.. _platform-agnostic:

Platform-agnostic
-----------------

Installation of Brightway2 has two steps. First, install the following scientific and numeric libraries:

* scipy >= 0.10
* numpy >= 1.6
* lxml
* pip

.. warning:: Make sure that ``SciPy`` builds with support for `UMFPACK <http://www.cise.ufl.edu/research/sparse/umfpack/>`_; you may need to also install `scikits-umpack <https://github.com/rc/scikit-umfpack>`_.

Second, install the Brightway2 package:

.. code-block:: bash

    pip install --user brightay2

.. _requirements:

Requirements
````````````

If you want to install packages manually, or not install everything, Brightway2 uses the following Python packages:

* appdirs
* asteval
* docopt
* eight
* flask
* future
* lxml
* numpy
* peewee
* psutil
* pyprind
* requests
* scipy
* stats_arrays
* unicodecsv
* voluptuous
* whoosh
* xlrd
* xlsxwriter

Developers
==========

.. warning:: If you are developing, it is *strongly* recommended to use `virtualenv <http://www.virtualenv.org/>`__ and `virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_ (or `virtualenv-win <https://github.com/davidmarble/virtualenvwrapper-win>`_ for Windows users).

If you want to develop with Brightway, then you should also install the following:

* nose
* sphinx

You can install editable Brightway2 packages using `mercurial <http://mercurial.selenic.com/>`_:

.. code-block:: bash

    pip install -e hg+https://bitbucket.org/cmutel/brightway2-data#egg=bw2data
    pip install -e hg+https://bitbucket.org/cmutel/brightway2-calc#egg=bw2calc
    pip install -e hg+https://bitbucket.org/cmutel/brightway2-ui#egg=bw2ui
    pip install -e hg+https://bitbucket.org/cmutel/brightway2-analyzer#egg=bw2analyzer

You can also simply clone the bitbucket source code repositories instead of installing them.

.. _developer-os-x:

Quickstart for OS X developers
------------------------------

Set up python:

.. code-block:: bash

    sudo port selfupdate
    sudo port install py27-scipy py27-numpy py27-pip py27-libxml2 py27-nose py27-sphinx py27-requests py27-flask py27-virtualenvwrapper mercurial +bash_completion
    sudo port select --set python python27
    sudo port select --set pip pip27
    sudo port select --set virtualenv virtualenv27

Change the shell to macports ``bash``. First, add the macports bash shell as a possibility:

.. code-block:: bash

    sudo -s
    # Type in your password here
    echo /opt/local/bin/bash >> /etc/shells
    exit

Then set your default shell

.. code-block:: bash

    chsh -s /opt/local/bin/bash

Add the following lines to the file ``.profile`` in your home directory using your favorite text editor:

.. code-block:: bash

    source /opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/virtualenvwrapper.sh

    if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
      . /opt/local/etc/profile.d/bash_completion.sh
    fi

You must then start a *new* terminal window, so the updated ``.profile`` is applied.

Create a `virtualenv <https://pypi.python.org/pypi/virtualenv>`__ and install Brightway2:

.. code-block:: bash

    mkvirtualenv bw2
    toggleglobalsitepackages
    pip install brightway2

Because this is using a virtualenv, you will need to activate the virtualenv each time you start a new terminal with:

.. code-block:: bash

    workon bw2

.. _upgrading:

Upgrading Brightway2
====================

Brightway2 is being actively developed, and new releases come frequently.

.. note:: Please subscribe to the `brightway2 updates mailing list <https://tinyletter.com/brightway2-updates>`_ to be informed of new releases.

To upgrade Brightway2, do the following:

First, make sure your background packages are up to date.

* In Enthought Canopy, this is done through the graphical package manager.
* In anaconda/miniconda, use the following commands (once you have activated your Brightway2 environment):

.. code-block:: bash

    conda update conda
    conda update anaconda

* In macports, use the following commands:

.. code-block:: bash

    sudo port selfupdate
    sudo port upgrade outdated

Next, run the following command. Make sure you are in the correct environment/virtualenv, if you use environments:

.. code-block:: bash

    pip install -U --no-deps brightway2 bw2data bw2calc bw2analyzer bw2ui bw2io bw2parameters

Finally, see if your data needs to be updated, and follow the instructions if it does:

.. code-block:: bash

    bw2-uptodate
