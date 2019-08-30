# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

@_curry1
def curry(fn):
    from .internal import getArgCount
    return curryN(getArgCount(fn), fn)
