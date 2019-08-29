# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def defaultTo(d, v):
    return v is None or d if v != v else v
