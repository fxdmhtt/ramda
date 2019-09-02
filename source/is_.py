# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def is_(Ctor, val):
    return val is not None and isinstance(val, Ctor)
