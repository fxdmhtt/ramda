# -*- coding: utf-8 -*-

from ..slice import slice

def _dropLastWhile(pred, xs):
    idx = len(xs) - 1
    while idx >= 0 and pred(xs[idx]):
        idx -= 1
    return slice(0, idx + 1, xs)
