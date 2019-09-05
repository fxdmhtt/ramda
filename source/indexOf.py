# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._indexOf import _indexOf
from .internal._isArray import _isArray

from .internal._getitem import _getitem

@_curry2
def indexOf(target, xs):
    indexOfFn = _getitem(xs, 'indexOf')
    return (
        indexOfFn(target) if callable(indexOfFn)
        else _indexOf(xs, target, 0)
    )
