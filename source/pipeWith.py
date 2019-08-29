# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2
from .head import head
from .internal._reduce import _reduce
from .tail import tail
from .identity import identity

@_curry2
def pipeWith(xf, list):
    if len(list) <= 0:
        return identity

    headList = head(list)
    tailList = tail(list)

    return _arity(len(headList), lambda *arguments: _reduce(
        lambda result, f: xf(f, result),
        headList(*arguments),
        tailList
    ))
