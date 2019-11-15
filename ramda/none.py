# -*- coding: utf-8 -*-

from .internal._complement import _complement
from .internal._curry2 import _curry2
from .all import all

@_curry2
def none(fn, input):
    return all(_complement(fn), input)
