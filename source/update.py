# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .adjust import adjust
from .always import always

@_curry3
def update(idx, x, list):
    return adjust(idx, always(x), list)
