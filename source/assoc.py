# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def assoc(prop, val, obj):
    result = {}
    for p in obj:
        result[p] = obj[p]
    result[prop] = val
    return result
