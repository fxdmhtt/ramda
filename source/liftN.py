# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._reduce import _reduce
from .ap import ap
from .curryN import curryN
from .map import map

@_curry2
def liftN(arity, fn):
    lifted = curryN(arity, fn)
    return curryN(arity, lambda *arguments: \
        _reduce(ap, map(lifted, arguments[0]), arguments[1:])
    )
