# -*- coding: utf-8 -*-

from .internal._reduce import _reduce
# from .internal._xwrap import _xwrap
from .curryN import curryN

def transduce(xf, fn, acc, list):
    return _reduce(xf(_xwrap(fn) if callable(fn) else fn), acc, list)
transduce = curryN(4, transduce)
