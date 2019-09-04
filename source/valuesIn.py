# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def valuesIn(obj):
    vs = []
    if isinstance(obj, dict):
        for prop in obj:
            vs.append(obj.get(prop))
    return vs
