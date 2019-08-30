# -*- coding: utf-8 -*-

from .internal._includesWith import _includesWith
from .internal._curry3 import _curry3

@_curry3
def differenceWith(pred, first, second):
    out = []
    idx = 0
    firstLen = len(first)
    while idx < firstLen:
        if not _includesWith(pred, first[idx], second) and \
           not _includesWith(pred, first[idx], out):
            out.append(first[idx])
        idx += 1
    return out

