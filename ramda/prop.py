# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .path import path

@_curry2
def prop(p, obj):
    return path([p], obj)
