# -*- coding: utf-8 -*-

from . import sig
from . import _apply, JSObject

def _arity(n, fn):
    if   n ==  0: return sig(names=[])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  1: return sig(names=['a0'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  2: return sig(names=['a0', 'a1'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  3: return sig(names=['a0', 'a1', 'a2'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  4: return sig(names=['a0', 'a1', 'a2', 'a3'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  5: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  6: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4', 'a5'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  7: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  8: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n ==  9: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    elif n == 10: return sig(names=['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'])(lambda *arguments: _apply(fn, JSObject(), arguments))
    else: raise ValueError('First argument to _arity must be a non-negative integer no greater than ten')
