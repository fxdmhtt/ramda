# -*- coding: utf-8 -*-

from .internal._objectAssign import _objectAssign
from .internal._curry1 import _curry1

@_curry1
def mergeAll(list):
    result = {}
    [result.update(d) for d in list]
    return _objectAssign(**result)
