# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._has import _has

@_curry1
def toPairs(obj):
    return obj.items()
