# -*- coding: utf-8 -*-

from ._forceReduced import _forceReduced
from ._isArrayLike import _isArrayLike
from ._reduce import _reduce
from ._xfBase import _xfBase

def preservingReduced(xf):
    def _transducer_step_function(result, input):
        ret = getattr(xf, '@@transducer/step')(result, input)
        return _forceReduced(ret) if getattr(ret, '@@transducer/reduced') else ret

    return {
        '@@transducer/init': _xfBase.init,
        '@@transducer/result': lambda result: \
            getattr(xf, '@@transducer/result')(result),
        '@@transducer/step': _transducer_step_function
    }

def _flatCat(xf):
    rxf = preservingReduced(xf)
    return {
        '@@transducer/init': _xfBase.init,
        '@@transducer/result': lambda result: \
            getattr(rxf, '@@transducer/result')(result),
        '@@transducer/step': lambda result, input: \
            _reduce(rxf, result, [input]) if not _isArrayLike(input) else _reduce(rxf, result, input)
    }
