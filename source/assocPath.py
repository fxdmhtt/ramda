# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .internal._has import _has
from .internal._isArray import _isArray
from .internal._isInteger import _isInteger
from .assoc import assoc
from .isNil import isNil

@_curry3
def assocPath(path, val, obj):
    if len(path) == 0:
        return val
    idx = path[0]
    if len(path) > 1:
        nextObj = (
            obj[idx] if not isNil(obj) and _has(idx, obj)
            else (
                [] if _isInteger(path[1])
                else {}
            )
        )
        val = assocPath(path[1:], val, nextObj)
    if _isInteger(idx) and _isArray(obj):
        arr = [] + obj
        if idx >= len(arr):
            arr += [None] * (idx - len(arr) + 1)
        arr[idx] = val
        return arr
    else:
        return assoc(idx, val, obj)
