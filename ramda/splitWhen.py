# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def splitWhen(pred, list):
    idx = 0
    len_ = len(list)

    while idx < len_ and not pred(list[idx]):
        idx += 1

    return [list[:idx], list[idx:]]
