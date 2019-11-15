# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def defaultTo(d, v):
    return d if v is None or v != v else v
