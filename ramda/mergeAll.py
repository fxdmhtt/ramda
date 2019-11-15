# -*- coding: utf-8 -*-

from .internal._objectAssign import _objectAssign
from .internal._curry1 import _curry1

@_curry1
def mergeAll(list):
    return _objectAssign({}, *list)
