# -*- coding: utf-8 -*-

from .internal._curryN import _curryN
from .internal._reduce import _reduce
from .internal._reduced import _reduced

def _reduceWhile(pred, fn, a, list):
    return _reduce(lambda acc, x: \
        fn(acc, x) if pred(acc, x) else _reduced(acc)
    , a, list)
reduceWhile = _curryN(4, [], function _reduceWhile)
