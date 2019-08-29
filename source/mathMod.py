# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isInteger import _isInteger

@_curry2
def mathMod(m, p):
    if not _isInteger(m): return float('nan')
    if not _isInteger(p) or p < 1: return float('nan')
    return ((m % p) + p) % p
