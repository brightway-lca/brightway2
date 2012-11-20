# -*- coding: utf-8 -*
import collections
import operator
import itertools

operators = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "is": operator.eq,
    "not": operator.ne,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
    "in": operator.contains,
    "notin": lambda x, y: not operator.contains(x, y),
    "iin": lambda x, y: x.lower() in y.lower(),
    "inot": lambda x, y: x.lower() != y.lower(),
    "iis": lambda x, y: x.lower() == y.lower(),
    "len": lambda x, y: len(x) == y,
}


def try_op(f, x, y):
    try:
        return f(x, y)
    except:
        return False


class Dictionaries(object):
    """A wrapper for a single call to iteritems() for multiple dictionaries.

    Useful for a ``Query`` across multiple databases."""
    def __init__(self, *args):
        self.dicts = args

    def iteritems(self):
        return itertools.chain(*[x.iteritems() for x in self.dicts])


class Result(object):
    """A container that wraps a filtered dataset. Returned by a calling a ``Query`` object. A result object functions like a read-only dictionary; you can call ``Result[some_key]``, or ``some_key in Result``, or ``len(Result)``.

    The dataset can also be sorted, using ``sort(field)``; the underlying data is then a ``collections.OrderedDict``.

    Args:
        * *result* (dict): The filtered dataset.

    """
    def __init__(self, result):
        self.result = result

    def __str__(self):
        return u"Query result with %i entries" % len(self.result)

    def __repr__(self):
        if len(self.result) > 20:
            data = dict([(key, self.result[key]) for key in \
                self.result.keys()[:20]])
        elif not len(self.result):
            return "Query result:\n\tNo query results found."
        else:
            data = self.result
        return "Query result: (total %i)\n" % len(self.result) \
            + "\n".join(["%s: %s" % (key, data[key]["name"]) for key in data])

    def sort(self, field, reverse=False):
        """Sort the filtered dataset. Operates in place; does not return anything.

        Args:
            * *field* (str): The key used for sorting.
            * *reverse* (bool, optional): Reverse normal sorting order.

        """
        self.result = collections.OrderedDict(sorted(self.result.iteritems(),
            key=lambda t: t[1].get(field, None), reverse=reverse))

    # Generic dictionary methods
    def __len__(self):
        return len(self.result)

    def __iter__(self):
        return iter(self.result)

    def keys(self):
        return self.result.keys()

    def iteritems(self):
        return self.result.iteritems()

    def __getitem__(self, key):
        return self.result[key]

    def __contains__(self, key):
        return key in self.result


class Query(object):
    """A container for a set of filters applied to a dataset.

    Filters are applied by calling the ``Query`` object, and passing the dataset to filter as the argument. Calling a ``Query`` with some data returns a ``Result`` object with the filtered dataset.

    Args:
        * *filters* (filters): One or more ``Filter`` objects.

    """
    def __init__(self, *filters):
        self.filters = list(filters)

    def add(self, filter_):
        """Add another filter.

        Args:
            *filter_* (``Filter``): A Filter object.

        """
        self.filters.append(filter_)

    def __call__(self, data):
        for filter_ in self.filters:
            data = filter_(data)
        return Result(data)


class Filter(object):
    """A filter on a dataset.

    The following functions are supported:

        * "<", "<=", "==", ">", ">=": Mathematical relations
        * "is", "not": Identity relations. Work on any Python object.
        * "in", "notin": List or string relations.
        * "iin", "iis", "inot": Case-insensitive string relations.
        * "len": Length relation.

    In addition, any function which defines a relationship between an input and an output can also be used.

    Examples:

        * All ``name`` values are *foo*: ``Filter("name", "is", "foo")``
        * All ``name`` values include the string *foo*: ``Filter("name", "in", "foo")``
        * Category (a list of categories and subcategories) includes *foo*: ``Filter("category", "in", "foo")``

    Args:
        * *key* (str): The field to filter on.
        * *function* (str or object): One of the pre-defined filters, or a callable object.
        * *value* (object): The value to test against.

    Returns:
        A ``Result`` object which wraps a new data dictionary.

    """
    def __init__(self, key, function, value):
        self.key = key
        self.function = function
        self.value = value
        if not callable(function):
            self.function = operators.get(function, None)
        if not self.function:
            raise ValueError("No valid function found")

    def __call__(self, data):
        return dict(((k, v) for k, v in data.iteritems() if try_op(
            self.function, v.get(self.key, None), self.value)))


# class Exchange(object):
#     def __init__(self, *args):
#         self.filters = args

#     def __call__(self, data):
#         """All filters should pass for at least one exchange"""
#         return dict([
#             (k, v) for k, v in data.iteritems() if \
#                 any([
#                     all([f.filter(e) for f in self.filters]) \
#                     for e in v["exchanges"]
#                 ])
#             ])
