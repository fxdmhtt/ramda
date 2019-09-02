# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1
from .map import map
from .max import max
from .reduce import reduce

from .internal import sig
from .internal import jsify

@_curry1
def cond(pairs):
    pairs = [(jsify(k), jsify(v)) for k, v in pairs]
    arity = reduce(
        max,
        0,
        map(lambda pair: pair[0].length, pairs)
    )
    @sig
    def function(*arguments):
        idx = 0
        while idx < len(pairs):
            if pairs[idx][0](*arguments):
                return pairs[idx][1](*arguments)
            idx += 1
    return _arity(arity, function)
