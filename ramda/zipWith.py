# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

from .internal import jsify
from .apply import apply

@_curry3
def zipWith(fn, a, b):
    return map(apply(jsify(fn)), zip(a, b))
