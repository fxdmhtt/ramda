# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .map import map

@_curry2
def lens(getter, setter):
    return lambda toFunctorFn: \
        lambda target, *args: \
            toFunctorFn(
                lambda focus, *args: \
                    setter(focus, target),
                getter(target)
            )
