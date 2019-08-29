# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1
from .map import map
from .max import max
from .reduce import reduce

@_curry1
def cond(pairs):
    arity = reduce(
        max,
        0,
        map(lambda pair: len(pair[0]), pairs)
    )
    def function(*arguments):
        idx = 0
        while (idx < len(pairs)):
            if pairs[idx][0](*arguments):
                return pairs[idx][1](*arguments)
            idx += 1
    return _arity(arity, function)
