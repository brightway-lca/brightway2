.. _uncertainty-type:

Storing uncertain values
========================

While some numeric data is certain, like unit conversions, real-world data is often uncertain. In Brightway2, uncertain data is stored in a ``uncertainty dictionary``.

An ``uncertainty dictionary`` is a python dictionary of keys and values, like:

.. code-block:: python

   {
      "Swiss chesse": "is awesome",
      "this is a key": "this is a value"
   }

It has one required key: ``amount``, which specifies the most representative value of the distribution. The most representative value can be the mean, median (like in the lognormal in the ecoinvent database), mode (like in the triangular in the ecoinvent database), or something else - the decision is up to you. The uncertainty distribution is defined by the key ``uncertainty type``.  Depending on the distribution, some or all of the following fields can also be specified: *loc*, *scale*, *shape*, *minimum*, and *maximum*.

The schema for an ``uncertainty dictionary`` in `voluptuous <https://pypi.python.org/pypi/voluptuous/>`_ is:

.. code-block:: python

    uncertainty_dict = {
        Required("amount"): Any(float, int),
        Optional("uncertainty type"): int,
        Optional("loc"): Any(float, int),
        Optional("scale"): Any(float, int),
        Optional("shape"): Any(float, int),
        Optional("minimum"): Any(float, int),
        Optional("maximum"): Any(float, int)
    }

The integer ``uncertainty type`` fields are defined in a separate software package called `stats_arrays <https://stats-arrays.readthedocs.org/en/latest/>`_. The uncertainty types are given below, and their parameters are explained in detail in the `stats_arrays table <https://stats-arrays.readthedocs.org/en/latest/#mapping-parameter-array-columns-to-uncertainty-distributions>`_:

    * ``0``: Undefined or unknown uncertainty.
    * ``1``: No uncertainty.
    * ``2``: Lognormal distribution. This is **purposely** handled in an inconsistent fashion, unfortunately. The ``amount`` field is the median of the data, and the ``sigma`` field is the standard deviation of the data **when it is log-transformed**, i.e. the σ from the formula for the log-normal PDF.
    * ``3``: Normal distribution.
    * ``4``: Uniform distribution.
    * ``5``: Triangular distribution.
    * ``6``: Bernoulli distribution.
    * ``7``: Discrete uniform.
    * ``8``: Weibull.
    * ``9``: Gamma.
    * ``10``: Beta distribution.
    * ``11``: Generalized Extreme Value.
    * ``12``: Student's T.

The default value for ``uncertainty type`` is ``0``, i.e. no uncertainty.

.. note::
    All distributions (where bounds make sense) can be bounded, i.e. you can specify a minimum and maximum value in addition to other parameters. This can be helpful in ensuring, for example, that distributions are always positive.

In most cases, if you don't have uncertainty, or don't know enough to be able to characterize that uncertainty, you can enter a number instead of an uncertainty dictionary, and it will be automatically converted to an uncertainty dictionary with no uncertainty.
