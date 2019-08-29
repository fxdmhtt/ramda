# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def insertAll(idx, elts, list):
    idx = idx < len(list) and (idx if idx >= 0 else len(list))
    return list[0:idx] + elts + list[idx:]
