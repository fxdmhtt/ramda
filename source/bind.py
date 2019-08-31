# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2

from .internal import sig
from .internal import length
from .internal import _apply

@_curry2
def bind(fn, thisObj):
    return _arity(length(fn), sig(lambda *arguments: \
        apply(fn, thisObj, arguments))
    )
