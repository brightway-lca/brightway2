Saving data to disk
*******************

Pickle is the default data storage format
=========================================

The Python standard library module `pickle <http://docs.python.org/2/library/pickle.html>`_ is the default data storage format?

The ``pickle`` module is fast, portable, and built-in. While using compression (such as gzip and bzip2) would reduce the size of the saved files, it also dramatically increases loading and saving times, by a factor of 3 - 30, depending on the test. Overall, the speed of ``pickle`` `seems to be fine <http://kbyanc.blogspot.ch/2007/07/python-serializer-benchmarks.html>`_.

Alternatives to pickle
----------------------

The ``marshal`` module is faster - 40% faster writing, 25% faster reading - but produces files twice as big, and can change from computer to computer or even when Python is upgraded. The costs and potential risks of ``marshal`` overwhelm its speed gains.

JSON
----

Javascript object notation (`JSON <http://json.org/>`_) is a data for native to `javascript <http://en.wikipedia.org/wiki/JavaScript>`_ which is now widely used for data exchange over the web and between different programming languages. ``JSON`` does not match perfectly to python data structures, but the differences are relatively small. ``JSON`` is used to store some metadata in Brightway2, such as the user preferences, LCI databases, and LCIA methods installed, as it is human readable and editable.

While a ``JSON`` module is in the standard library, there is no fast ``JSON`` library available for all operating systems and python version; see e.g. `anyjson <http://pypi.python.org/pypi/anyjson/>`_, `yajl <http://pypi.python.org/pypi/yajl>`_, and `ujson <http://pypi.python.org/pypi/ujson/>`_, in addition to the builtin.
