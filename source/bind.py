# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2

@_curry2
def bind(fn, thisObj):
    from .internal import getArgCount
    return _arity(getArgCount(fn), lambda *arguments: \
        fn(*arguments)
    )
