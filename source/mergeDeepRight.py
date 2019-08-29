# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .mergeDeepWithKey import mergeDeepWithKey

@_curry2
def mergeDeepRight(lObj, rObj):
    return mergeDeepWithKey(lambda k, lVal, rVal: rVal, lObj, rObj)
