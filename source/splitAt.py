# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .length import length
from .slice import slice

@_curry2
def splitAt(index, array):
    return [slice(0, index, array), slice(index, length(array), array)]
