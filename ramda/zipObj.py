# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from .fromPairs import fromPairs

@_curry2
def zipObj(keys, values):
    return fromPairs(zip(keys, values))
