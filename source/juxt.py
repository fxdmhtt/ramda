# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .converge import converge

from .internal import sig

@_curry1
def juxt(fns):
    return converge(sig(lambda *arguments: arguments[0:]), fns)
