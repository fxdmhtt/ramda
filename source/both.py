# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .and_ import and_
from .lift import lift

@_curry2
def both(f, g):
    return (
        lambda *arguments: f(*arguments) and g(*arguments) if _isFunction(f)
        else lift(and_)(f, g)
    )
