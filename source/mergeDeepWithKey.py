# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .internal._isObject import _isObject
from .mergeWithKey import mergeWithKey

@_curry3
def mergeDeepWithKey(fn, lObj, rObj):
    return mergeWithKey(lambda k, lVal, rVal: \
        mergeDeepWithKey(fn, lVal, rVal) \
        if _isObject(lVal) and _isObject(rVal) \
        else fn(k, lVal, rVal)
    , lObj, rObj)
