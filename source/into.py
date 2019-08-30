# -*- coding: utf-8 -*-

from .internal._clone import _clone
from .internal._curry3 import _curry3
from .internal._isTransformer import _isTransformer
from .internal._reduce import _reduce
from .internal._stepCat import _stepCat

@_curry3
def into(acc, xf, list):
    return (
        _reduce(xf(acc), acc['@@transducer/init'](), list) if _isTransformer(acc)
        else _reduce(xf(_stepCat(acc)), _clone(acc, [], [], false), list)
    )
