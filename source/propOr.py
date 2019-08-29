# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .pathOr import pathOr

@_curry3
def propOr(val, p, obj):
    return pathOr(val, [p], obj)
