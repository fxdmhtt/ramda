# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

from .insertAll import insertAll

@_curry3
def insert(idx, elt, list):
    return insertAll(idx, [elt], list)
