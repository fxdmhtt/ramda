# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def reduceRight(fn, acc, list):
    idx = len(list) - 1
    while idx >= 0:
        acc = fn(list[idx], acc)
        idx -= 1
    return acc
