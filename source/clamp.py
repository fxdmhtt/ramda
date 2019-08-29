# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def clamp(min, max, value):
    if min > max:
        raise ValueError('min must not be greater than max in clamp(min, max, value)')
    return (
        min if value < min else
        max if value > max else value
    )
