# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

Const = lambda x: \
    {'value': x, 'fantasy-land/map': lambda: None}

@_curry2
def view(lens, x):
    return lens(Const)(x).value
