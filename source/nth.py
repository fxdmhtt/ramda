# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isString import _isString

@_curry2
def nth(offset, list):
    idx = len(list) + offset if offset < 0 else offset
    return list[idx] if _isString(list) else list[idx]
