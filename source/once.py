# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1

from .internal import sig
from .internal import length
from .internal import _apply, JSObject

@_curry1
def once(fn):
    called = False
    result = None
    @sig
    def function(*arguments):
        nonlocal result
        if called:
            return result
        called = True
        result = _apply(fn, JSObject(), arguments)
        return result
    return _arity(length(fn), function)
