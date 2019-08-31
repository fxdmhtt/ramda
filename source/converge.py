# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._map import _map
from .curryN import curryN
from .max import max
from .pluck import pluck
from .reduce import reduce

from .internal import sig
from .internal import length
from .internal import jsify

@_curry2
def converge(after, fns):
    fns = [jsify(fn) for fn in fns]
    @sig
    def function(*arguments):
        args = arguments
        return after(*_map(lambda fn: \
            fn(*args)
        , fns))
    return curryN(reduce(max, 0, (length(fn) for fn in fns)), function)
