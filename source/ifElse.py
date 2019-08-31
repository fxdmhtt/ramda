# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .curryN import curryN

from .internal import sig
from .internal import length
from .internal import _apply, JSObject

@_curry3
def ifElse(condition, onTrue, onFalse):
    return curryN(max(length(condition), length(onTrue), length(onFalse)),
        sig(lambda *arguments: \
            _apply(onTrue, JSObject(), arguments) if _apply(condition, JSObject(), arguments) else _apply(onFalse, JSObject(), arguments))
    )
