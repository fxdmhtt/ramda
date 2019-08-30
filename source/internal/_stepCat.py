# -*- coding: utf-8 -*-

from ._objectAssign import _objectAssign
from ._identity import _identity
from ._isArrayLike import _isArrayLike
from ._isTransformer import _isTransformer
from ..objOf import objOf

_stepCatArray = {
    '@@transducer/init': list,
    '@@transducer/step': lambda xs, x: \
        (
            xs.append(x),
            xs,
        )[-1],
    '@@transducer/result': _identity
}
_stepCatString = {
    '@@transducer/init': str,
    '@@transducer/step': lambda a, b: a + b,
    '@@transducer/result': _identity
}
_stepCatObject = {
    '@@transducer/init': dict,
    '@@transducer/step': lambda result, input: \
        _objectAssign(
            result,
            objOf(input[0], input[1]) if _isArrayLike(input) else input
        ),
    '@@transducer/result': _identity
}

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
