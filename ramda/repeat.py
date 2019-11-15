# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .always import always
from .times import times

@_curry2
def repeat(value, n):
    return times(always(value), n)
