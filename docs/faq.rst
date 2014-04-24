Frequently Asked Questions
**************************

What text editor or IDE should I use?
=====================================

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

Why the 2 in Brightway2?
========================

Brightway version 1 was a set of programs written during the PhD of Chris Mutel. In the end, there wasn't that much that could be re-used from this research code, other than the name. Brightway2 is a completely new software framework designed to avoid the fate of Brightway version 1. See also the `blog post on technical motivation <http://chris.mutel.org/brightway2-technical-motivation.html>`_.

Data formats
============

Why are activity dataset keys so confusing? `('ecoinvent 2.2', '5bbf2e66f2d75d60726974ac44ab4225')` seems insane!
-----------------------------------------------------------------------------------------------------------------

It is insane, in the sense that it doesn't make any sense at all to people. Rather, `5bbf2e66f2d75d60726974ac44ab4225` is a computer-generated unique ID. The basic problem is that we need one unique ID for an activity dataset, but there is no ID provided in the ecospold 1 data format. Instead, an activity is uniquely identified by its name, location, category, subcategory, unit, and whether or not it is an infrastructure process! `5bbf2e66f2d75d60726974ac44ab4225` is just an easy way of representing all this information in one string. It is a pain, but there is no good way around it.

Unfortunately, ecospold 2 (the data format used in ecoinvent 3) isn't more approachable - keys will now look like `('ecoinvent 3', 'fff06f42-6c5f-4aea-b695-93bcaba55fed')`. Sorry. At least this time it is ecoinvent generating the unique ID, and not Brightway2.

For an easier way to work with activities on the command line, see `Tutorial 2a - Using bw2simple to make life easier <http://nbviewer.ipython.org/url/brightwaylca.org/tutorials/Tutorial 2a - Using bw2simple to make life easier.ipynb>`_, based on the helper package `bw2simple <https://bitbucket.org/cmutel/brightway2-simple>`_.

Why pickle? Serialization *X* is so much better!
------------------------------------------------

Well, Windows people in particular have slow load times, but also pain in installing things, so adding new dependencies is strongly discouraged. Things like message pack and JSON can't handle all Python datatypes, and in particular Python allows tuples as dictionary keys, which we use heavily, while others don't. So, pickle is the default format, even though it is not the hawtness... However, JSON is used as a backup format, as pickle has real drawbacks for archiving.

See also:

    * `OMG msgpack FTW! <http://msgpack.org/>`_
    * `No it isn't shut up <https://news.ycombinator.com/item?id=4090831>`_
    * `JSON speed depends heavily on JSON library <http://liangnuren.wordpress.com/2012/08/13/python-json-performance/>`_
    * `Speed comparison - cPickle is actually pretty fast <http://www.justinfx.com/2012/07/25/python-2-7-3-serializer-speed-comparisons/>`_
    * `Screw it, let's use HDF5 <https://github.com/telegraphic/hickle>`_

Also, google for how every new JSON library which has great promise (e.g. `uJSON <https://pypi.python.org/pypi/ujson>`_, `YAJL <http://lloyd.github.io/yajl/>`_, etc., etc.) is subtly incompatible or broken in some key ways with the actual JSON spec.

Problems
========

I get unicode errors!
---------------------

A typical error message is:

.. code-block:: python

    UnicodeEncodeError: 'ascii' codec can't encode character u'\xe1' in position 426: ordinal not in range(128)

The problem here is that python tries to convert a character from unicode to an encoding which doesn't support that character. A common default encoding in python 2.X is ascii, which doesn't support much. You can fix this by changing the default encoding:

.. code-block:: python

    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")

See also:

    * `PrintFails <https://wiki.python.org/moin/PrintFails>`_
    * `Why does Python print unicode characters when the default encoding is ASCII? <http://stackoverflow.com/questions/2596714/why-does-python-print-unicode-characters-when-the-default-encoding-is-ascii>`_
    * `IPython Notebook: What is the default encoding? <http://stackoverflow.com/questions/15420672/ipython-notebook-what-is-the-default-encoding>`_
    * `Absolute minimum everyone should know about Unicode <http://www.joelonsoftware.com/articles/Unicode.html>`_

The global warming potential values are different in SimaPro!
-------------------------------------------------------------

The default LCIA characterization factors in Brightway2 come from version 2 of the ecoinvent database. For most LCIA methods, these are identical to those found in SimaPro. However, there are important differences for global warming potential:

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
