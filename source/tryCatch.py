# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._concat import _concat
from .internal._curry2 import _curry2

from .internal import sig
from .internal import jsify
from .internal import length

@_curry2
def tryCatch(tryer, catcher):
    @sig
    def function(*arguments):
        try:
            return jsify(tryer)(*arguments)
        except Exception as e:
            return jsify(catcher)(*_concat([e], arguments))
    return _arity(length(tryer), function)
