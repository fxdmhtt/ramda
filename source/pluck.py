# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .map import map
from .prop import prop

@_curry2
def pluck(p, list):
    return map(prop(p), list)
