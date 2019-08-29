# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2
from .internal._has import _has

@_curry2
def memoizeWith(mFn, fn):
    cache = {}
    def function(*arguments):
        key = mFn(*arguments)
        if not _has(key, cache):
            cache[key] = fn(*arguments)
        return cache[key]
    return _arity(fn.__code__.co_argcount, function)
