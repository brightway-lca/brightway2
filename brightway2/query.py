# -*- coding: utf-8 -*
import collections


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
    def __init__(self, field, value):
        self.field = field
        self.value = value

    def __call__(self, data):
        """Should return a filtered dictionary, same form as before"""
        return dict((k, v) for k, v in data.iteritems() if self.filter(v))

    def filter(self, o):
        raise NotImplemented


# class Category(object):
#     def __init__(self, *args):
#         self.filters = args

#     def __call__(self, data):
#         return dict([
#             (k, v) for k, v in data.iteritems() if \
#                 all([
#                     any([f.filter(x) for x in v["categories"]]) \
#                     for f in self.filters
#                 ])
#             ])


class Exchange(object):
    def __init__(self, *args):
        self.filters = args

    def __call__(self, data):
        """All filters should pass for at least one exchange"""
        return dict([
            (k, v) for k, v in data.iteritems() if \
                any([
                    all([f.filter(e) for f in self.filters]) \
                    for e in v["exchanges"]
                ])
            ])


class In(Filter):
    def filter(self, o):
        return self.value in o.get(self.field, [])


class Is(Filter):
    def filter(self, o):
        return self.value == o.get(self.field, "")


class Isnt(Filter):
    def filter(self, o):
        return self.value != o.get(self.field, None)


class Contains(Filter):
    def filter(self, o):
        return self.value in o.get(self.field, None)


class iFilter(Filter):
    def __init__(self, field, value):
        self.field = field
        self.value = value.lower()


class iIs(iFilter):
    def filter(self, o):
        return self.value == o.get(self.field, "").lower()


class iIsnt(iFilter):
    def filter(self, o):
        return self.value != o.get(self.field, "").lower()


class iIn(iFilter):
    def filter(self, o):
        return self.value in [x.lower() for x in o.get(self.field, [])]


class iContains(iFilter):
    def filter(self, o):
        return self.value in (o.get(self.field, '').lower() or None)
