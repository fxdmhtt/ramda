# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def insert(idx, elt, list):
    idx = idx < len(list) and (idx if idx >= 0 else len(list))
    result = list[0:]
    result = result[:idx] + elt + result[idx + 0:]
    return result
