# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pick(names, obj):
    return {k: obj[k] for k in names if k in obj}
