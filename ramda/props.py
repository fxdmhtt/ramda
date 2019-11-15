# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .path import path

@_curry2
def props(ps, obj):
    return list(map(lambda p: \
        path([p], obj)
    , ps))
