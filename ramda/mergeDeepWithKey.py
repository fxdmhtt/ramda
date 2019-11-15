# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .internal._isObject import _isObject
from .mergeWithKey import mergeWithKey

@_curry3
def mergeDeepWithKey(fn, lObj, rObj):
    def function(k, lVal, rVal):
        if _isObject(lVal) and _isObject(rVal):
            return mergeDeepWithKey(fn, lVal, rVal)
        else:
            return fn(k, lVal, rVal)
    return mergeWithKey(function, lObj, rObj)
