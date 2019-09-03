# -*- coding: utf-8 -*-

from .internal._Set import _Set
from .internal._curry2 import _curry2

@_curry2
def uniqBy(fn, list):
    set = _Set()
    result = []
    idx = 0

    while idx < len(list):
        item = list[idx]
        appliedItem = fn(item)
        if appliedItem not in set:
            set.add(appliedItem)
            result.append(item)
        idx += 1
    return result
