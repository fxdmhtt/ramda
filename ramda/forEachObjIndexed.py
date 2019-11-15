# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .keys import keys

from .internal import jsify

@_curry2
def forEachObjIndexed(fn, obj):
    fn = jsify(fn)
    list(map(lambda pair: fn(pair[1], pair[0], obj), obj.items()))
    return obj
