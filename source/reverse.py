# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isString import _isString

@_curry1
def reverse(list):
    return list[::-1]
