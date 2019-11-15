# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .pipeWith import pipeWith

@_curry2
def composeWith(xf, list_):
    return pipeWith(xf, reversed(list_))
