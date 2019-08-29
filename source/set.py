# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .always import always
from .over import over

@_curry3
def set(lens, v, x):
    return over(lens, always(v), x)
