# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from .internal import _apply, JSObject

@_curry2
def apply(fn, args):
    return _apply(fn, JSObject(), args)
