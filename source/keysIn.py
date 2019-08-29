# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def keysIn(obj):
    ks = []
    for prop in obj:
        ks.append(prop)
    return ks
