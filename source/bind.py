# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2

@_curry2
def bind(fn, thisObj):
    import inspect
    return _arity(len(inspect.signature(fn).parameters), lambda *arguments: \
        fn(*arguments)
    )
