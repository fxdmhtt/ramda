# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .keys import keys

@_curry1
def values(obj):
    props = keys(obj)
    len_ = len(props)
    vals = []
    idx = 0
    while idx < len_:
        vals.append(obj[props[idx]])
        idx += 1
    return vals
