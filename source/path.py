# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .paths import paths

@_curry2
def path(pathAr, obj):
    return paths([pathAr], obj)[0]
