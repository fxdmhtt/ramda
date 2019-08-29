# -*- coding: utf-8 -*-

from .internal._objectAssign import _objectAssign
from .internal._curry2 import _curry2

@_curry2
def mergeLeft(l, r):
    return _objectAssign({}, r, l)
