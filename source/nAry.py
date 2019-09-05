# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from .internal import jsify

@_curry2
def nAry(n, fn):
    if   n ==  0: return jsify(lambda *_: jsify(fn)())
    elif n ==  1: return jsify(lambda a0, *_: jsify(fn)(a0))
    elif n ==  2: return jsify(lambda a0, a1, *_: jsify(fn)(a0, a1))
    elif n ==  3: return jsify(lambda a0, a1, a2, *_: jsify(fn)(a0, a1, a2))
    elif n ==  4: return jsify(lambda a0, a1, a2, a3, *_: jsify(fn)(a0, a1, a2, a3))
    elif n ==  5: return jsify(lambda a0, a1, a2, a3, a4, *_: jsify(fn)(a0, a1, a2, a3, a4))
    elif n ==  6: return jsify(lambda a0, a1, a2, a3, a4, a5, *_: jsify(fn)(a0, a1, a2, a3, a4, a5))
    elif n ==  7: return jsify(lambda a0, a1, a2, a3, a4, a5, a6, *_: jsify(fn)(a0, a1, a2, a3, a4, a5, a6))
    elif n ==  8: return jsify(lambda a0, a1, a2, a3, a4, a5, a6, a7, *_: jsify(fn)(a0, a1, a2, a3, a4, a5, a6, a7))
    elif n ==  9: return jsify(lambda a0, a1, a2, a3, a4, a5, a6, a7, a8, *_: jsify(fn)(a0, a1, a2, a3, a4, a5, a6, a7, a8))
    elif n == 10: return jsify(lambda a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, *_: jsify(fn)(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9))
    else: raise ValueError('First argument to nAry must be a non-negative integer no greater than ten')
