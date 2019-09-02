# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xdrop import _xdrop
from .slice import slice

@_curry2
def drop(n, xs):
    import sys
    return slice(max(0, n), sys.maxsize, xs)
