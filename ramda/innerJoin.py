# -*- coding: utf-8 -*-

from .internal._includesWith import _includesWith
from .internal._curry3 import _curry3
from .internal._filter import _filter

@_curry3
def innerJoin(pred, xs, ys):
    return _filter(lambda x: _includesWith(pred, x, ys), xs)
