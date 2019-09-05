# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .slice import slice

@_curry2
def dropLast(n, list):
    return slice(None, -max(0, n) or None, list)
