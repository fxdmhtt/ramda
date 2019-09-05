# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._Set import _Set

@_curry2
def difference(first, second):
    out = []
    idx = 0
    firstLen = len(first)
    toFilterOut = set(second)

    while idx < firstLen:
        if first[idx] not in toFilterOut:
            toFilterOut.add(first[idx])
            out.append(first[idx])
        idx += 1
    return out
