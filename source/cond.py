# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1
from .map import map
from .max import max
from .reduce import reduce

from .internal import sig
from .internal import _apply, JSObject

@_curry1
def cond(pairs):
    arity = reduce(
        max,
        0,
        map(lambda pair: len(pair[0]), pairs)
    )
    @sig
    def function(*arguments):
        idx = 0
        while idx < len(pairs):
            if _apply(pairs[idx][0], JSObject(), arguments):
                return _apply(pairs[idx][1], JSObject(), arguments)
            idx += 1
    return _arity(arity, function)
