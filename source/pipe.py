# -*- coding: utf-8 -*-

from .internal._arity import _arity
from .internal._pipe import _pipe
from .reduce import reduce
from .tail import tail

def pipe(*arguments):
    if len(arguments) == 0:
        raise ValueError('pipe requires at least one argument')
    return _arity(
        arguments[0].__code__.co_argcount,
        reduce(_pipe, arguments[0], tail(arguments))
    )
