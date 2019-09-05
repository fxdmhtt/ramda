# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def aperture(n, list):
    for idx in range(len(list) - (n - 1)):
        yield list[idx:idx + n]
