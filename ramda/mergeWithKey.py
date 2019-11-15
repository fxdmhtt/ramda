# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .internal._has import _has

@_curry3
def mergeWithKey(fn, l, r):
    result = {}

    for k in l:
        if _has(k, l):
            result[k] = fn(k, l[k], r[k]) if _has(k, r) else l[k]

    for k in r:
        if _has(k, r) and not _has(k, result):
            result[k] = r[k]

    return result
