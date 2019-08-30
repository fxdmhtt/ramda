# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .mergeDeepWithKey import mergeDeepWithKey

@_curry3
def mergeDeepWith(fn, lObj, rObj):
    return mergeDeepWithKey(lambda k, lVal, rVal: \
        fn(lVal, rVal)
    , lObj, rObj)
