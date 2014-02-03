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


