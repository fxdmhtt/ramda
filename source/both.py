# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .and_ import and_
from .lift import lift

from .internal import sig
from .internal import _apply, JSObject

@_curry2
def both(f, g):
    return (
        sig(lambda *arguments: _apply(f, JSObject(), arguments) and _apply(g, JSObject(), arguments)) if _isFunction(f)
        else lift(and_)(f, g)
    )
