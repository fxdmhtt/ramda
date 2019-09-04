# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def dissoc(prop, obj):
    result = {}
    for p in obj or {}:
        result[p] = obj[p]
    if prop in result:
        del result[prop]
    return result
