# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .liftN import liftN

@_curry1
def lift(fn):
    from .internal import getArgCount
    return liftN(getArgCount(fn), fn)
