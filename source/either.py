# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .lift import lift
from .or_ import or_

from .internal import sig
from .internal import _apply, JSObject

@_curry2
def either(f, g):
    return (
        sig(lambda *arguments: _apply(f, JSObject(), arguments) or _apply(g, JSObject(), arguments)) if _isFunction(f)
        else lift(or_)(f, g)
    )
