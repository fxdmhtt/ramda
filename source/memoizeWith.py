# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2
from .internal._has import _has

from .internal import sig
from .internal import length
from .internal import _apply, JSObject

@_curry2
def memoizeWith(mFn, fn):
    cache = {}
    @sig
    def function(*arguments):
        key = _apply(mFn, JSObject(), arguments)
        if not _has(key, cache):
            cache[key] = _apply(fn, JSObject(), arguments)
        return cache[key]
    return _arity(length(fn), function)
