# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xtap import _xtap

def tap(fn, x):
    fn(x)
    return x
tap = _curry2(_dispatchable([], _xtap, tap))
