# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._reduce import _reduce
from .keys import keys

from .internal import jsify

@_curry2
def mapObjIndexed(fn, obj):
    fn = jsify(fn)
    return {k: fn(obj[k], k, obj) for k in obj}
