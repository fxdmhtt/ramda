# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def valuesIn(obj):
    vs = []
    for prop in obj:
        vs.append(obj[prop])
    return vs
