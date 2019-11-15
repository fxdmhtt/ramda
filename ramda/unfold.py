# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def unfold(fn, seed):
    pair = fn(seed)
    while pair and len(pair):
        yield pair[0]
        pair = fn(pair[1])
