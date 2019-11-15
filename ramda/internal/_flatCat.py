# -*- coding: utf-8 -*-

# from ._forceReduced import _forceReduced
from ._isArrayLike import _isArrayLike
from ._reduce import _reduce
from ._xfBase import _xfBase

def preservingReduced(xf):
    def function(result, input):
        ret = xf(result, input)
        return ret
    return function

def _flatCat(xf):
    rxf = preservingReduced(xf)
    return lambda result, input: \
        (
            _reduce(rxf, result, [input]) if not _isArrayLike(input)
            else _reduce(rxf, result, input)
        )
