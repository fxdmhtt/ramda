# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def o(f, g, x):
    return f(g(x))
