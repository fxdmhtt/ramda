# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

@_curry1
def curry(fn):
    import inspect
    return curryN(len(inspect.signature(fn).parameters), fn)
