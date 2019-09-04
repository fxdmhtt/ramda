# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from .internal import jsify

@_curry2
def mapIndexed(fn, obj):
    fn = jsify(fn)
    for idx, x in enumerate(obj):
        yield fn(x, idx, obj)
