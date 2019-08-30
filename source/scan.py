# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def scan(fn, acc, list):
    idx = 0
    len_ = len(list)
    result = [acc]
    while idx < len_:
        acc = fn(acc, list[idx])
        result.append(acc)
        idx += 1
    return result
