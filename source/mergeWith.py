# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .mergeWithKey import mergeWithKey

@_curry3
def mergeWith(fn, l, r):
    return mergeWithKey(lambda _, _l, _r: \
        fn(_l, _r)
    , l, r)
