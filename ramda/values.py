# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .keys import keys

@_curry1
def values(obj):
    for prop in keys(obj):
        yield obj[prop]
