# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isNumber import _isNumber

@_curry2
def range(from_, to):
    if not (_isNumber(from_) and _isNumber(to)):
        raise TypeError('Both arguments to range must be numbers')

    import builtins
    return list(builtins.range(from_, to))
