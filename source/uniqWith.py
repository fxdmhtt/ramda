# -*- coding: utf-8 -*-

from .internal._includesWith import _includesWith
from .internal._curry2 import _curry2

@_curry2
def uniqWith(pred, list):
    idx = 0
    len_ = len(list)
    result = []
    while idx < len_:
        item = list[idx]
        if not _includesWith(pred, item, result):
            result.append(item)
        idx += 1
    return result
