# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .nAry import nAry

@_curry1
def unary(fn):
    return nAry(1, fn)
