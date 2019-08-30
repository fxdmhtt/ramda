# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._concat import _concat
from .internal._curry2 import _curry2

@_curry2
def tryCatch(tryer, catcher):
    def function(*arguments):
        try:
            return tryer(*arguments)
        except Exception as e:
            return catcher(*_concat([e], arguments))
    from .internal import getArgCount
    return _arity(getArgCount(tryer), function)
