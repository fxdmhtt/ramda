# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isArray import _isArray
from .apply import apply
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce
from .keys import keys
from .values import values

def mapValues(fn, obj):
    return (
        map(fn, obj) if _isArray(obj)
        else keys(obj).reduce(lambda acc, key: \
            (
                acc.__setitem__(key, fn(obj[key])),
                acc
            )[-1]
        , {})
    )

@_curry1
def applySpec(spec):
    spec = mapValues(
        lambda v: v if callable(v) else applySpec(v),
        spec
    )

    def function(*arguments):
        args = arguments
        return mapValues(lambda f: apply(f, args), spec)
    import inspect
    return curryN(
        reduce(max, 0, (len(inspect.signature(fn).parameters) for fn in values(spec))),
        function
    )
