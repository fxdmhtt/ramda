# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pick(names, obj):
    result = {}
    idx = 0
    while idx < len(names):
        if names[idx] in obj:
            result[names[idx]] = obj[names[idx]]
        idx += 1
    return result
