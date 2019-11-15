# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .defaultTo import defaultTo
from .path import path

@_curry3
def pathOr(d, p, obj):
    return defaultTo(d, path(p, obj))
