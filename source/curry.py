# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN

from .internal import length

@_curry1
def curry(fn):
    return curryN(length(fn), fn)
