# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .curryN import curryN

@_curry3
def ifElse(condition, onTrue, onFalse):
    import inspect
    return curryN(max(len(inspect.signature(condition).parameters), len(inspect.signature(onTrue).parameters), len(inspect.signature(onFalse).parameters)),
        lambda *arguments: \
            onTrue(*arguments) if condition(*arguments) else onFalse(*arguments)
    )
