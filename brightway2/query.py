# -*- coding: utf-8 -*
import collections
import operator

operators = {
    "<": operator.lt,
    "<=": operator.le,
    "==": operator.eq,
    "is": operator.eq,
    "!=": operator.ne,
    ">=": operator.ge,
    ">": operator.gt,
    "in": operator.contains,
    "nin": lambda x, y: not operator.contains(x, y),
    "iin": lambda x, y: x.lower() in y.lower()
}


def try_op(f, x, y):
    try:
        return f(x, y)
    except:
        return False


class Result(object):
    """The result of a query"""
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

    def __getitem__(self, key):
        return self.result[key]

    def __contains__(self, key):
        return key in self.result

    def sort(self, field):
        self.result = collections.OrderedDict(sorted(self.result.iteritems(),
            key=lambda t: t[1].get(field, None)))

    def __len__(self):
        return len(self.result)


class Query(object):
    """A Database or Method query."""
    def __init__(self, *queries):
        self.queries = list(queries)

    def add(self, query):
        self.queries.append(query)

    def __call__(self, data):
        for query in self.queries:
            data = query(data)
        return Result(data)


class Filter(object):
    def __init__(self, key, value, function):
        self.key = key
        self.value = value
        self.function = function
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
