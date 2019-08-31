# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2
from .head import head
from .internal._reduce import _reduce
from .tail import tail
from .identity import identity

from .internal import sig
from .internal import length
from .internal import _call, _apply, JSObject

@_curry2
def pipeWith(xf, list):
    if len(list) <= 0:
        return identity

    headList = head(list)
    tailList = tail(list)

    return _arity(length(headList), sig(lambda *arguments: \
        _reduce(
            lambda result, f: \
                _call(xf, JSObject(), f, result),
            _apply(headList, JSObject(), arguments),
            tailList
        ))
    )
