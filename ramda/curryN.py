# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1
from .internal._curry2 import _curry2
from .internal._curryN import _curryN

@_curry2
def curryN(length, fn):
    if length == 1:
        return _curry1(fn)
    return _arity(length, _curryN(length, [], fn))
