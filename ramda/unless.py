# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def unless(pred, whenFalseFn, x):
    return x if pred(x) else whenFalseFn(x)
