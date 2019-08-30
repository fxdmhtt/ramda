# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isInteger import _isInteger
from .nth import nth

@_curry2
def paths(pathsArray, obj):
    def function(paths):
        val = obj
        idx = 0
        while idx < len(paths):
            if val is None:
                return
            p = paths[idx]
            val = nth(p, val) if _isInteger(p) else val[p]
            idx += 1
        return val
    return list(map(function, pathsArray))
