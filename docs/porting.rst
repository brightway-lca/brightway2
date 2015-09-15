Python 3 porting strategy
=========================

Brightway2 is written for python 3.4, but runs on python 2.7 as well. Tests are run against both 2.7 and 3.4. Python 3 versions less than 3.4 are not supported.

The library `eight <https://github.com/kislyuk/eight>`__ is used to forward-port python 2.7 code to 3.4. This means that ``super``, ``str``, and ``bytes`` have 3.4 semantics. The print function and true division are imported from ``__future__``, as are ``unicode_literals``.

See also:

* `Common migration problems <http://python3porting.com/problems.html>`__
* `FTFY - library to fix common encoding problems <https://github.com/LuminosoInsight/python-ftfy>`__
