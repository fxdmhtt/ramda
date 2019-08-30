# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .curryN import curryN

@_curry3
def ifElse(condition, onTrue, onFalse):
    from .internal import getArgCount
    return curryN(max(getArgCount(condition), getArgCount(onTrue), getArgCount(onFalse)),
        lambda *arguments: \
            onTrue(*arguments) if condition(*arguments) else onFalse(*arguments)
    )
