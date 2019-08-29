# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .map import map

@_curry2
def lens(getter, setter):
    return lambda toFunctorFn: \
        return lambda target: \
            return map(
                lambda focus: \
                    setter(focus, target),
                toFunctorFn(getter(target))
            )
