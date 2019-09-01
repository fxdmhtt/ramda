# -*- coding: utf-8 -*-

from .internal._clone import _clone
from .internal._curry3 import _curry3
from .internal._reduce import _reduce
# from .internal._stepCat import _stepCat

@_curry3
def into(acc, xf, list):
    return _reduce(xf, _clone(acc, [], [], false), list)
