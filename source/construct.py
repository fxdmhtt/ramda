# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .constructN import constructN

@_curry1
def construct(Fn):
    from .internal import getArgCount
    return constructN(getArgCount(Fn), Fn)
