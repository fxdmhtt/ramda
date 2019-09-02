# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._equals import _equals

@_curry2
def equals(a, b):
    return _equals(a, b, [], [])
