# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .keys import keys

@_curry2
def forEachObjIndexed(fn, obj):
    keyList = keys(obj)
    idx = 0
    while idx < len(keyList):
        key = keyList[idx]
        fn(obj[key], key, obj)
        idx += 1
    return obj
