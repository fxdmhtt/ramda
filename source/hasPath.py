# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._has import _has

from .isNil import isNil

@_curry2
def hasPath(_path, obj):
    if len(_path) == 0 or isNil(obj):
        return False
    val = obj
    idx = 0
    while idx < len(_path):
        if not isNil(val) and _has(_path[idx], val):
            val = val[_path[idx]]
            idx += 1
        else:
            return False
    return True
