# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .path import path

@_curry3
def pathSatisfies(pred, propPath, obj):
    return pred(path(propPath, obj))
