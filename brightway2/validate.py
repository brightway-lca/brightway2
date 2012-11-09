# encoding: utf-8
try:
    from voluptuous import Schema, required
except:
    raise ImportError("The voluptuous package is required for validation")

db_validator = Schema({tuple: {
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
        required("sigma"): float,
        required("technosphere"): bool,
        required("uncertainty type"): int
        }]
    }},
    extra=True)
