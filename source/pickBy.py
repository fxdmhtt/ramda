# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pickBy(test, obj):
    result = {}
    for prop in obj:
        if test(obj[prop], prop, obj):
            result[prop] = obj[prop]
    return result
