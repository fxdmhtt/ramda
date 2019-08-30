# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._map import _map
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

@_curry2
def converge(after, fns):
    def function(*arguments):
        args = arguments
        return after(*_map(lambda fn: \
            fn(*args)
        , fns))
    import inspect
    return curryN(reduce(max, 0, (len(inspect.signature(fn).parameters) for fn in fns)), function)
