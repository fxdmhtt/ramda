# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def isNil(x):
    return x is None
