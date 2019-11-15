# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._has import _has
from .keys import keys

@_curry1
def invert(obj):
    props = keys(obj)
    len_ = len(props)
    idx = 0
    out = {}

    while idx < len_:
        key = props[idx]
        val = obj[key]
        if _has(val, out):
            list = out[val]
        else:
            list = out[val] = []
        list.append(key)
        idx += 1
    return out
