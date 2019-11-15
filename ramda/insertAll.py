# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def insertAll(idx, elts, list):
    idx = idx if 0 <= idx < len(list) else len(list)
    return list[:idx] + elts + list[idx:]
