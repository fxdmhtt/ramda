# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xtake = None
from .slice import slice

def take(n, xs):
    import sys
    return slice(0, sys.maxsize if n < 0 else n, xs)
take = _curry2(_dispatchable(['take'], _xtake, take))
