# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .constructN import constructN

from .internal import length

@_curry1
def construct(Fn):
    return constructN(length(Fn), Fn)
