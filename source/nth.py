# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isString import _isString

@_curry2
def nth(offset, list):
    idx = (len(list) + offset) if offset < 0 else offset
    return None if idx < 0 else list[idx]
