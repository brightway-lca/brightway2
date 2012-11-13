# encoding: utf-8
try:
    from voluptuous import Schema, required, Invalid
except:
    raise ImportError("The voluptuous package is required for validation")


def valid_tuple(o):
    try:
        assert isinstance(o, tuple)
        assert isinstance(o[0], basestring)
        assert isinstance(o[1], (basestring, int, tuple, list))
    except:
        raise Invalid("The key %s is invalid" % o)
    return o

db_validator = Schema({valid_tuple: {
    required("code"): object,
    "categories": list or tuple,
    "location": object,
    required("name"): basestring,
    required("type"): "process" or "emission" or "process",
    "unit": basestring,
    required("exchanges"): [{
        required("amount"): float,
        required("input"): object,
        "pedigree matrix": basestring,
        "code": object,
        "sigma": float,
        required("technosphere"): bool,
        required("uncertainty type"): int
        }]
    }},
    extra=True)

ia_validator = Schema({valid_tuple: float})
