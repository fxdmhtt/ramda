# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def any(fn, list):
    import builtins
    return builtins.any(map(fn, list))
