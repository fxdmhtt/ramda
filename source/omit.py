# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def omit(names, obj):
    return {k: v for k, v in obj.items() if k not in names}
