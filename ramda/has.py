# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .hasPath import hasPath

@_curry2
def has(prop, obj):
    return hasPath([prop], obj)
