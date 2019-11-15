# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def dissoc(prop, obj):
    result = obj and dict(obj) or {}
    if prop in result:
        del result[prop]
    return result
