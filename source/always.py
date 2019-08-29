# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def always(val):
    return lambda *_: val
