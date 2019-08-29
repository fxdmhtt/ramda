# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .equals import equals
from .takeLast import takeLast

@_curry2
def endsWith(suffix, list):
    return equals(takeLast(len(suffix), list), suffix)
