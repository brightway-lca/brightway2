Frequently Asked Questions
**************************

Why the 2 in Brightway2?
========================

Brightway version 1 was a set of programs written during the PhD of Chris Mutel. In the end, there wasn't that much that could be re-used from this research code, other than the name. Brightway2 is a completely new software framework designed to avoid the fate of Brightway version 1. See also the `blog post on technical motivation <http://chris.mutel.org/brightway2-technical-motivation.html>`_.

General Python questions
========================

What text editor or IDE should I use?
-------------------------------------

When you are doing more complex work, it is often nice to work with an intelligent text editor or an integrated development environment (IDE).

Here are some text editors which are often recommended:

    * `Sublime text <http://www.sublimetext.com/>`_
    * `Notepad ++ <http://notepad-plus-plus.org/>`_
    * Native editors like gedit or notepad

Here are some IDEs which are often recommended:

    * `Spyder <https://code.google.com/p/spyderlib/>`_
    * `PyCharm <http://www.jetbrains.com/pycharm/>`_
    * `PyDev + Eclipse <http://pydev.org/>`_
    * `Komodo <http://www.activestate.com/python-ide>`_
    * `WingWare <http://wingware.com/>`_

See also the `discussion on the Python wiki <https://wiki.python.org/moin/IntegratedDevelopmentEnvironments>`_ and a `long StackOverflow discussion <http://stackoverflow.com/questions/81584/what-ide-to-use-for-python/>`_.

Data management
===============

Which ecoinvent file should I download?
---------------------------------------

Ecoinvent makes several versions of each system model available:


* ecoinvent 3.3_xxx_ecoSpold02.7z
* ecoinvent 3.3_xxx_lci_ecoSpold02.7z
* ecoinvent 3.3_xxx_lcia_ecoSpold02.7z
* ecoinvent 3.3_xxx_lcia-cumulated-matrices_xls.7z
* ecoinvent 3.3_xxx_lci-cumulated-matrices_xls.7z

You want to download and import ``ecoinvent 3.3_xxx_ecoSpold02.7z``. If your import process is taking a long time or a lot of memory, double check to make sure you have the right version.

How do I resolve errors about read-only projects?
-------------------------------------------------

Brightway2 uses the `fasteners <https://pypi.python.org/pypi/fasteners>`__ library to create lock files that conflicts in written data. More specifically, when you use ``projects.set_current`` to `switch to a new project <https://bitbucket.org/cmutel/brightway2-data/src/default/bw2data/project.py?at=default&fileviewer=file-view-default#project.py-141>`__, Brightway will read a bunch of metadata about things like project databases and LCIA methods into memory. It will then try to acquire a lock that gives it the exclusive right to change this metadata in the future. If a second Python kernel switches to the same project, it will load the latest saved version of the metadata, and will then fail to acquire the lock, so will be set to read-only mode (i.e. ``projects.read_only = True``).

This locking was introduced because people were having trouble with multiple people working on the same project and getting conflicts or even corruption in the metadata. The problem is easy to understand - if two kernels load the metadata into memory, and each make a change somewhere, then whoever saves the latest will overwrite the changes of the other.

You can run into problems if a Python kernel is not shut down properly. To be safe, you should **always manually shut down** each Python shell and each Jupyter notebook. In extreme cases, it may be necessary to manually delete the lock file or restart your computer.

If you are sure that it is safe to write data, then you can trick the ``projects`` object into allowing writes - just set ``projects.read_only = False``. But be careful that you only do this in a single Python kernel.

How do I backup my data?
------------------------

Each project is just a subdirectory (you can get the path using ``projects.dir``), and this can be backed up using any normal tools, including cloud backups like Dropbox.

You can save a snapshot of entire project directory with ``backup_data_directory``, or save a single project with ``backup_project_directory``. Both functions return the filepath of the created archive file.

You can also:

* Save any data object (like a ``Database`` or ``Method``) to a ``BW2Package`` using ``BW2Package.export_objs``.
* Export a database to Excel using ``bw2io.export.excel.write_lci_activities``.

How do I find where my data is saved?
-------------------------------------

You can find the current project data directory with the command ``projects.dir``; everything will be stored in this folder or a subdirectory. Similarly, you can find the logs directory with the command ``projects.logs_dir``.

Brightway2 uses the `appdirs <https://pypi.python.org/pypi/appdirs/1.4.0>`__ library to select an appropriate, platform-specific path, namely:

    * On Windows: ``C:\Documents and Settings\<User>\Application Data\Local Settings\pylca\Brightway2``
    * On OS X: ``/Users/<User>/Library/Application Support/Brightway2``
    * On Linux: ``/home/<User>/.local/share/Brightway2``

You can specify a custom data directory path by setting the environment variable ``BRIGHTWAY2_DIR`` , but this is not recommended for normal use, unless you have multiple installations of brightway2 and want to have a separate data directory for each.

Setting ``BRIGHTWAY2_DIR`` in a virtual environment
```````````````````````````````````````````````````

When you create a virtual environment, it lives in a folder that by default is something like ``<YOUR_ANACONDA_INSTALL_DIR>/envs/<YOUR_ENV_NAME>``.  When conda activates or deactivates an environment, it looks for additional scripts in the two subfolders ``activate.d`` and ``deactivate.d`` within this folder. When virtualenv activates or deactivates an environment, it uses the scripts ``activate`` and ``deactivate`` in ``<YOUR_ENV>\bin\``.

When using conda, to set the persistent environment variables in the virtual environment, do the following. If using virtualenv, instructions are roughly similar but will need some adaptation.

1.Navigate into your virtual environment folders just doing (both Mac/Linux and Windows):

.. code-block:: bash

    cd <YOUR_ANACONDA_INSTALL_DIR>/envs/<YOUR_ENV_NAME>

2.Create the two aforementioned folders.

* For Mac/Linux, type in the terminal:

.. code-block:: bash

    mkdir -p etc/conda/activate.d
    mkdir -p etc/conda/deactivate.d

* For Windows the command to make folders is slightly different :

.. code-block:: bash

    mkdir etc\conda\activate.d
    mkdir etc\conda\deactivate.d

3.Create scripts in those folders that set and unset the environment variables (in this case ``BRIGHTWAY2_DIR``). The names of the files don't matter, but the file extensions do.

* For Mac and Linux, the extension must be ``.sh`` files. Inside the folder ``activate.d`` create the file ``whatever_name_you_like.sh`` and inside it write ``export BRIGHTWAY2_DIR=/my/custom/directory`` while in ``activate.d`` create ``whatever_name_you_like.sh`` and inside write ``unset BRIGHTWAY2_DIR``.
* For Windows the procedure is exactly the same, you just need to change the file extension from ``.sh`` into ``.bat`` i.e. instead of ``whatever_name_you_like.sh`` use ``whatever_name_you_like.bat``

How can I rename projects?
--------------------------

You can't. However, you can quickly copy a project to the new name (``projects.copy_project("my new name")``), and then delete the original (``projects.delete_project("old name")``).

Data formats
============

Why are activity dataset keys so confusing? `('ecoinvent 2.2', '5bbf...')` seems insane!
-----------------------------------------------------------------------------------------------------------------

It is insane, in the sense that it doesn't make any sense at all to people. Rather, `5bbf2e66f2d75d60726974ac44ab4225` is a computer-generated unique ID. The basic problem is that we need one unique ID for an activity dataset, but there is no ID provided in the ecospold 1 data format. Instead, an activity is uniquely identified by its name, location, category, subcategory, unit, and whether or not it is an infrastructure process! `5bbf2e66f2d75d60726974ac44ab4225` is just an easy way of representing all this information in one string. It is a pain, but there is no good way around it.

Unfortunately, ecospold 2 (the data format used in ecoinvent 3) isn't more approachable - keys will now look like `('ecoinvent 3', 'fff06f42-6c5f-4aea-b695-93bcaba55fed')`. Sorry. At least this time it is ecoinvent generating the unique ID, and not Brightway2.

Why pickle? Serialization *X* is so much better!
------------------------------------------------

The Python standard library module `pickle <http://docs.python.org/2/library/pickle.html>`_ is the default data storage format for most data. Windows people in particular have slow load times, but also pain in installing things, so adding new dependencies is strongly discouraged.

The ``pickle`` module is fast, portable, and built-in. While using compression (such as gzip and bzip2) would reduce the size of the saved files, it also dramatically increases loading and saving times, by a factor of 3 - 30, depending on the test. Overall, the speed of ``pickle`` `seems to be fine <http://kbyanc.blogspot.ch/2007/07/python-serializer-benchmarks.html>`_.

The ``marshal`` module is faster - 40% faster writing, 25% faster reading - but produces files twice as big, and can change from computer to computer or even when Python is upgraded. The costs and potential risks of ``marshal`` overwhelm its speed gains.

Javascript object notation (`JSON <http://json.org/>`_) is a data for native to `javascript <http://en.wikipedia.org/wiki/JavaScript>`_ which is now widely used for data exchange over the web and between different programming languages. ``JSON`` does not match perfectly to python data structures, but the differences are relatively small. ``JSON`` is used to store some metadata in Brightway2, such as the user preferences, and the installed LCI databases and LCIA methods. JSON is human readable and editable.

While a ``JSON`` module is in the standard library, there is no fast ``JSON`` library available for all operating systems and python version; see e.g. `anyjson <http://pypi.python.org/pypi/anyjson/>`__, `yajl <http://pypi.python.org/pypi/yajl>`__, and `ujson <http://pypi.python.org/pypi/ujson/>`__, in addition to the builtin `json <https://docs.python.org/2/library/json.html>`__. Each of these libraries is also not 100% compliant with the JSON spec.

Things like message pack and JSON can't handle all Python datatypes, and in particular Python allows tuples as dictionary keys, which we use heavily, while others don't. So, pickle is the default format, even though it is not the hawtness... However, JSON is used as a backup format, as pickle has real drawbacks for archiving.

See also:

    * `OMG msgpack FTW! <http://msgpack.org/>`_
    * `No it isn't shut up <https://news.ycombinator.com/item?id=4090831>`_
    * `JSON speed depends heavily on JSON library <http://liangnuren.wordpress.com/2012/08/13/python-json-performance/>`_
    * `Speed comparison - cPickle is actually pretty fast <http://www.justinfx.com/2012/07/25/python-2-7-3-serializer-speed-comparisons/>`_
    * `Screw it, let's use HDF5 <https://github.com/telegraphic/hickle>`_

.. _whysqlite:

Storing Python objects in a SQLite3 database is silly! Why not use *X* document database?
-----------------------------------------------------------------------------------------

Where *X* is one of `MongoDB <https://www.mongodb.com>`__, `CouchDB <http://couchdb.apache.org/>`__, `UnQLite <https://unqlite-python.readthedocs.io/en/latest/>`__, `Vedis <https://vedis-python.readthedocs.io/en/latest/>`__, `CDB <https://cr.yp.to/cdb.html>`__, `TinyDB <http://tinydb.readthedocs.io/en/latest/intro.html>`__, etc.

This approach may seem strange at first, but is the result of coding, evaluating, and ultimately rejecting several alternatives. Most document databases can't store all Python objects directly, because they use JSON or some other serialization. We have actually built and tested database backends built on pickle files, JSON files, `MongoDB <https://www.mongodb.com>`__, `CodernityDB <http://labs.codernity.com/codernitydb/>`__, and `BlitzDB <http://blitzdb.readthedocs.io/en/latest/>`__. SQLite3 also has several real advantages:

* Most importantly, it is included with Python, no new dependencies or installation steps are required.
* It is famous for being well tested, and is completely cross-platform.
* It is also more than fast enough. For example, loading every activity from ecoinvent 3+ takes only a few seconds.

Problems
========

I found a bug! What now?
------------------------

First, please check the list of :ref:`knownissues`. However, if your issue isn't listed, by all means please `create a bug report <https://bitbucket.org/cmutel/brightway2/issues/new>`__. Here is some good advice on creating a `short, self contained, correct example <http://sscce.org/>`__ for a bug report.

It is too slow!
---------------

* Install the `brightway2-speedups library <https://pypi.python.org/pypi/bw2speedups>`_. It will produce significant time savings in LCA calculations.
* Install `scikits-umfpack <https://github.com/stefanv/umfpack>`_ for faster LCA calculations.
* Install `anyjson <https://pypi.python.org/pypi/anyjson>`_ and `python-cjson <https://pypi.python.org/pypi/python-cjson>`_.

If your numerical work after LCA calculations is slow, consider the `numexpr <https://github.com/pydata/numexpr>`_ and `Bottleneck <https://pypi.python.org/pypi/Bottleneck>`_ libraries.

I get unicode errors!
---------------------

.. note:: All strings should be unicode. In Python 2.7, they have a 'u' in front of the string, like ``u"foo"``; in Python 3, all strings are unicode. If you are careful to make sure your data is unicode, you shouldn't have this problem.

.. note:: You can specify the encoding of text in your python files as UTF-8 by putting the following as the *first line* in each file: ``# -*- coding: utf-8 -*-``

A typical error message is:

.. code-block:: python

    UnicodeEncodeError: 'ascii' codec can't encode character u'\xe1' in position 426: ordinal not in range(128)

The problem here is that python tries to convert a character from unicode to an encoding which doesn't support that character. A common default encoding in python 2.X is ascii, which doesn't support much. You can fix this by changing the default encoding:

.. code-block:: python

    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

For understanding the difference between bytestrings and unicode:

First, read `What actually changed in the text model between Python 2 and Python 3? <http://python-notes.curiousefficiency.org/en/latest/python3/questions_and_answers.html#what-actually-changed-in-the-text-model-between-python-2-and-python-3>`__ - a very understandable and detailed description of what the title says.

Then, see the following resources:

    * `PrintFails <https://wiki.python.org/moin/PrintFails>`_
    * `Why does Python print unicode characters when the default encoding is ASCII? <http://stackoverflow.com/questions/2596714/why-does-python-print-unicode-characters-when-the-default-encoding-is-ascii>`_
    * `IPython Notebook: What is the default encoding? <http://stackoverflow.com/questions/15420672/ipython-notebook-what-is-the-default-encoding>`_
    * `Absolute minimum everyone should know about Unicode <http://www.joelonsoftware.com/articles/Unicode.html>`_

For help in fixing strings:

    * `FTFY - library to fix common encoding problems <https://github.com/LuminosoInsight/python-ftfy>`__ with accompanying blog post: `Fixing Unicode mistakes and more: the ftfy package <http://blog.luminoso.com/2012/08/24/fixing-unicode-mistakes-and-more-the-ftfy-package/>`_
    * `Is there a way to determine the encoding of text file? <http://stackoverflow.com/questions/436220/python-is-there-a-way-to-determine-the-encoding-of-text-file>`_
    * `Chardet: The Universal Character Encoding Detector <https://pypi.python.org/pypi/chardet>`_

When upgrading on Windows, I get errors about something called ``vcvarsall.bat``
--------------------------------------------------------------------------------

.. note:: The :ref:`upgrading` docs avoid this problem by always using ``pip`` with ``--no-deps``.

The problem here is that ``pip -U install foo`` will try to upgrade all dependencies of ``foo``. If, for example, scipy is a dependency, and a newer version is available, then pip will try to compile it. Compilation of scipy requires a C compiler, which is why python looks for ``vcvarsall.bat``, which you don't have.

If you are using something like conda, you should first make sure that all of your libraries are up to date already. Usually they will build the difficult packages so that you don't have to. In many cases, this should solve the problem, as you will then have the latest version of your dependencies.

If this doesn't solve the problem, then you have two options:

First, you can tell pip not to update all the dependencies. For example, to get the latest version of ``foo``, you would run:

.. code-block:: bash

    pip install -U --no-deps foo

Second, you can try to install a C compiler. You can find `decent instructions online <http://shop.wickeddevice.com/2013/12/11/windows-7-python-virtualenv-and-the-unable-to-find-vcvarsall-bat-error/>`_, as well as discussion on `Stack <http://stackoverflow.com/questions/3047542/building-lxml-for-python-2-7-on-windows/5122521#5122521>`_ `Overflow <http://stackoverflow.com/questions/6551724/how-do-i-point-easy-install-to-vcvarsall-bat>`_.

The global warming potential values are different in SimaPro!
-------------------------------------------------------------

The default LCIA characterization factors in Brightway2 come from version 3.2 of the ecoinvent database. For most LCIA methods, these are identical to those found in SimaPro. However, there are important differences for global warming potential:

1. SimaPro does not include a characterization factors for carbon monoxide, but ecoinvent does. Here is the ecoinvent language:

    Emitted CO is transformed in the atmosphere to |CO2| after some time. Not all LCIA methods do consider the global warming potential of CO. Most methods are based on factors published by the IPCC (IPCC 2001). It is assumed that |CO2| emissions are calculated with the carbon content of the burned fuels and thus all carbon in the fuel is considered. In ecoinvent CO emissions are subtracted from the theoretical |CO2| emissions. Thus a GWP factor is calculated for CO (1.57 kg |CO2|-eq per kg CO). Otherwise processes with higher CO emissions would benefit from this gap. This is especially important for biomass combustion. Neglecting the formation of CO2 from CO would lead in this case to a negative sum of the global warming potential score.

The value of 1.57 is the ratio of the molecular weights of |CO2| and CO.


2. SimaPro gives biogenic methane a characterization factor of 22 kg |CO2|-eq, while ecoinvent gives 25, the same value as for other types of methane.

.. note:: There may be other differences as well - these are the ones we have found.

.. |CO2| replace:: CO\ :sub:`2`

References:

* `IPCC third assessment report <http://www.ipcc.ch/ipccreports/tar/wg1/249.htm>`_
* `IPCC fourth assessment report <http://www.ipcc.ch/publications_and_data/ar4/wg1/en/ch2s2-10-3-2.html>`_
* `SimaPro method manual <http://www.pre-sustainability.com/download/DatabaseManualMethods-oct2013.pdf>`_ (see page 38)
* `ecoinvent report <http://www.ecoinvent.org/fileadmin/documents/en/03_LCIA-Implementation-v2.2.pdf>`_ (see page 26)

Why do I get negative results in ecoinvent 3?
---------------------------------------------

Depending on the LCIA method and functional unit, some LCA scores might be negative. Not everything is bad for the environment in every impact category!
