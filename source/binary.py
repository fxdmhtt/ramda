# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal.nAry import nAry

@_curry1
def binary(fn):
    return nAry(2, fn)
