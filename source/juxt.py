# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .converge import converge

@_curry1
def juxt(fns):
    return converge(lambda *arguments: arguments, fns)
