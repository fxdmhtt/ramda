# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .curryN import curryN

@_curry3
def ifElse(condition, onTrue, onFalse):
    return curryN(Math.max(condition.__code__.co_argcount, onTrue.__code__.co_argcount, onFalse.__code__.co_argcount),
        lambda *arguments: onTrue(*arguments) if condition(*arguments) else onFalse(*arguments)
    )
