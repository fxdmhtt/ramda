# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def toPairsIn(obj):
    pairs = []
    for prop in obj:
        pairs.append([prop, obj[prop]])
    return pairs
