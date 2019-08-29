# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .empty import empty
from .equals import equals

@_curry1
def isEmpty(x):
    return x is not None and equals(x, empty(x))
