# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

Identity = lambda fn, xs: list(map(fn, xs))

@_curry3
def over(lens, f, x):
    return lens(Identity)(x)
