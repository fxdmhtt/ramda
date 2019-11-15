# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._curry2 import _curry2
from .head import head
from .internal._reduce import _reduce
from .tail import tail
from .identity import identity

from .internal import sig
from .internal import length

@_curry2
def pipeWith(xf, list_):
    list_ = list(list_)
    if len(list_) <= 0:
        return identity

    headList = head(list_)
    tailList = tail(list_)

    return _arity(length(headList), lambda *arguments: \
        _reduce(
            lambda result, f: \
                xf(f, result),
            headList(*arguments),
            tailList
        )
    )
