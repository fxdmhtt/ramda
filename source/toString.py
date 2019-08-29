# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._toString import _toString

@_curry1
def toString(val):
    return _toString(val, [])
