# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .slice import slice

@_curry2
def splitEvery(n, list):
    if n <= 0:
        raise ValueError('First argument to splitEvery must be a positive integer')
    result = []
    idx = 0
    while idx < len(list):
        result.append(slice(idx, idx + n, list))
        idx += n
    return result
