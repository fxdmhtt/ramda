# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isFunction import _isFunction
from .lift import lift
from .or_ import or_

@_curry2
def either(f, g):
    return (
        lambda *arguments: f(*arguments) or g(*arguments) if _isFunction(f)
        else lift(or_)(f, g)
    )
