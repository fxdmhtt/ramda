# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

Identity = lambda x: \
    {'value': x, 'map': lambda f: Identity(f(x))}

@_curry3
def over(lens, f, x):
    return lens(lambda y: Identity(f(y)))(x).value
