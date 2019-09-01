# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .curryN import curryN

from .internal import sig
from .internal import length

@_curry3
def ifElse(condition, onTrue, onFalse):
    return curryN(max(length(condition), length(onTrue), length(onFalse)),
        sig(lambda *arguments: \
            onTrue(*arguments) if condition(*arguments) else onFalse(*arguments))
    )
