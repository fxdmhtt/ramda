# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._reduce import _reduce
from .keys import keys

from .internal import jsify

@_curry2
def mapObjIndexed(fn, obj):
    return _reduce(lambda acc, key: \
        (
            acc.__setitem__(key, jsify(fn)(obj[key], key, obj)),
            acc
        )[-1]
    , {}, keys(obj))
