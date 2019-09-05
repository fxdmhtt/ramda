# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isString import _isString

@_curry2
def nth(offset, list):
    try:
        return list[offset]
    except IndexError:
        return '' if isinstance(list, str) else None
