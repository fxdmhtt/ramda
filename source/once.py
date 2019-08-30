# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry1 import _curry1

@_curry1
def once(fn):
    called = False
    result = None
    def function(*arguments):
        nonlocal result
        if called:
            return result
        called = True
        result = fn(*arguments)
        return result
    return _arity(fn.__code__.co_argcount, function)
