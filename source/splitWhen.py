# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def splitWhen(pred, list):
    idx = 0
    len = len(list)
    prefix = []

    while idx < len and not pred(list[idx]):
        prefix.append(list[idx])
        idx += 1

    return [prefix, list[idx:]]
