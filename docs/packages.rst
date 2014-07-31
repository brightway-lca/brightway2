.. _packages:

Brightway2 Packages
===================

Brightway2 is split into several packages, where each package fulfills a certain role in the framework. The idea is that you can be an expert on a certain package, but not have to learn anything about other packages.

Core packages
-------------

brightway2
~~~~~~~~~~

This manual, plus a generic container that imports from brightway2-data and brightway2-calc.

* `source code <https://bitbucket.org/cmutel/brightway2>`__
* `documentation <https://brightway2.readthedocs.org/en/latest/>`__

brightway2-data
~~~~~~~~~~~~~~~

This package provides facilities for managing LCI databases and LCIA methods, as well as input and output scripts.

* `source code <https://bitbucket.org/cmutel/brightway2-data>`__
* `documentation <https://bw2data.readthedocs.org/en/latest/>`__
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/data/index.html>`__

brightway2-calc
~~~~~~~~~~~~~~~

This package provides classes for LCA calculations, both static and uncertain, and basic regionalized LCA.

* `source code <https://bitbucket.org/cmutel/brightway2-calc>`__
* `documentation <https://brightway2-calc.readthedocs.org/en/latest/>`__
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/calc/index.html>`__

brightway2-analyzer
~~~~~~~~~~~~~~~~~~~

This package provides functions for interpreting and analyzing LCI databases, LCIA methods, and LCA results.

* `source code <https://bitbucket.org/cmutel/brightway2-analyzer>`__
* `documentation <https://bw2analyzer.readthedocs.org/en/latest/>`__
* `report on how well the tests cover the code base <http://coverage.brightwaylca.org/analyzer/index.html>`__

brightway2-ui
~~~~~~~~~~~~~

This package provides both command line and web user interfaces.

* `source code <https://bitbucket.org/cmutel/brightway2-ui>`__

Secondary packages
------------------

These packages are extensions to Brightway2, and have lower standards for documentation and test coverage. They show how Brightway2 can be extended into new areas of LCA.

brightway2-regional
~~~~~~~~~~~~~~~~~~~

Full-fledged regionalization in Brightway2.

* `source code <https://bitbucket.org/cmutel/brightway2-regional>`__
* `documentation <https://brightway2-regional.readthedocs.org/en/latest/>`__

brightway2-temporalis
~~~~~~~~~~~~~~~~~~~~~

Dynamic LCA in Brightway2.

* `source code <https://bitbucket.org/cmutel/brightway2-temporalis>`__
* `documentation <https://brightway2-temporalis.readthedocs.org/en/latest/>`__

brightway2-restapi
~~~~~~~~~~~~~~~~~~

A simple `REST <http://en.wikipedia.org/wiki/Representational_state_transfer>`_ `API <http://en.wikipedia.org/wiki/Application_programming_interface>`_ for Brightway2 LCI data.

* `source code <https://bitbucket.org/cmutel/brightway2-restapi>`__
* `documentation <http://brightway2-restapi.readthedocs.org/en/latest/>`__
* `100% test coverage <http://coverage.brightwaylca.org/restapi/index.html>`__

brightway2-simple
~~~~~~~~~~~~~~~~~

Easier use of Brightway2 objects in the python shell/ipython notebook.

* `source code <https://bitbucket.org/cmutel/brightway2-simple>`__
* `documentation <http://brightway2-simple.readthedocs.org/en/latest/>`__
* `video <https://www.youtube.com/watch?v=n0UN9nj_mag>`__
