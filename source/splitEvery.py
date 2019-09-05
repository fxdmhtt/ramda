# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .slice import slice

@_curry2
def splitEvery(n, list):
    if n <= 0:
        raise ValueError('First argument to splitEvery must be a positive integer')
    for idx in range(0, len(list), n):
        yield slice(idx, idx + n, list)
