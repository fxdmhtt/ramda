# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry2 import _curry2

def intersperse(separator, list):
    out = []
    idx = 0
    length = len(list)
    while idx < length:
        if idx == length - 1:
            out.append(list[idx])
        else:
            out.extend([list[idx], separator])
        idx += 1
    return out
intersperse = _curry2(_checkForMethod('intersperse', intersperse))
