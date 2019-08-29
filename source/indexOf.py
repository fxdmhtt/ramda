# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._indexOf import _indexOf
from .internal._isArray import _isArray

@_curry2
def indexOf(target, xs):
    return (
        xs.indexOf(target)
        if callable(getattr(xs, 'indexOf', None)) and not _isArray(xs)
        else _indexOf(xs, target, 0)
    )
