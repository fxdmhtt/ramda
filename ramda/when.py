# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def when(pred, whenTrueFn, x):
    return whenTrueFn(x) if pred(x) else x
