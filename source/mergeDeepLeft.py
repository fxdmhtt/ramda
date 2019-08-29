# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .mergeDeepWithKey import mergeDeepWithKey

@_curry2
def mergeDeepLeft(lObj, rObj):
    return mergeDeepWithKey(lambda k, lVal, rVal: lVal, lObj, rObj)
