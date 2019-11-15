# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def all(fn, list):
    import builtins
    return builtins.all(map(fn, list))
