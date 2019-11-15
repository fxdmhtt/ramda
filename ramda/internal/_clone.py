# -*- coding: utf-8 -*-

from ..type import type

def _clone(value, refFrom, refTo, deep):
    import copy
    return copy.deepcopy(value) if deep else copy.copy(value)
