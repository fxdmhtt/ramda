# -*- coding: utf-8 -*-

from ._objectAssign import _objectAssign
from ._identity import _identity
from ._isArrayLike import _isArrayLike
from ._isTransformer import _isTransformer
from ..objOf import objOf

_stepCatArray = lambda xs, x: \
    xs.append(x) or xs
_stepCatString = lambda a, b: a + b
_stepCatObject = lambda result, input: \
    _objectAssign(
        result,
        objOf(input[0], input[1]) if _isArrayLike(input) else input
    )

def _stepCat(obj):
    if _isTransformer(obj):
        return obj
    if _isArrayLike(obj):
        return _stepCatArray
    if isinstance(obj, str):
        return _stepCatString
    if isinstance(obj, dict):
        return _stepCatObject
    raise ValueError('Cannot create transformer for ' + obj)
