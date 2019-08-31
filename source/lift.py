# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .liftN import liftN

from .internal import length

@_curry1
def lift(fn):
    return liftN(length(fn), fn)
