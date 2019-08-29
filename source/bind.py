# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2

@_curry2
def bind(fn, thisObj):
    return _arity(fn.__code__.co_argcount, lambda *arguments: fn(*arguments))
