# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .slice import slice

@_curry2
def drop(n, xs):
    return slice(max(0, n), None, xs)
