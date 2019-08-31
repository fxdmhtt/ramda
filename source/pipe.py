# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._pipe import _pipe
from .reduce import reduce
from .tail import tail

from .internal import sig
from .internal import length

@sig
def pipe(*arguments):
    if len(arguments) == 0:
        raise ValueError('pipe requires at least one argument')
    return _arity(
        length(arguments[0]),
        reduce(_pipe, arguments[0], tail(arguments))
    )
