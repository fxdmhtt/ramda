# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._has import _has

@_curry1
def toPairs(obj):
    pairs = []
    for prop in obj:
        if _has(prop, obj):
            pairs.append([prop, obj[prop]])
    return pairs
