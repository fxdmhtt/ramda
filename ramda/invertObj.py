# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .keys import keys

@_curry1
def invertObj(obj):
    props = keys(obj)
    len_ = len(props)
    idx = 0
    out = {}

    while idx < len_:
        key = props[idx]
        out[obj[key]] = key
        idx += 1
    return out
