# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pickAll(names, obj):
    return {k: obj.get(k) for k in names}
