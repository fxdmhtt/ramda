# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .equals import equals

@_curry3
def eqBy(f, x, y):
    return equals(f(x), f(y))
