# -*- coding: utf-8 -*-

from .internal._clone import _clone
from .internal._curryN import _curryN
from .internal._dispatchable import _dispatchable
from .internal._has import _has
from .internal._reduce import _reduce
from .internal._xreduceBy import _xreduceBy

def reduceBy(valueFn, valueAcc, keyFn, list):
    def function(acc, elt):
        key = keyFn(elt)
        acc[key] = valueFn(acc[key] if _has(key, acc) else _clone(valueAcc, [], [], False), elt)
        return acc
    return _reduce(function, {}, list)
reduceBy = _curryN(4, [], _dispatchable([], _xreduceBy, reduceBy))
