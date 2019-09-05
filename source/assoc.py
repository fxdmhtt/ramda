# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def assoc(prop, val, obj):
    result = obj and dict(obj) or {}
    result[prop] = val
    return result
