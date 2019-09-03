# -*- coding: utf-8 -*-

from ..type import type

def _clone(value, refFrom, refTo, deep):
    import copy
    return copy.deepcopy(value) if deep else copy.copy(value)

    def copy(copiedValue):
        len_ = len(refFrom)
        idx = 0
        while idx < len_:
            if value == refFrom[idx]:
                return refTo[idx]
            idx += 1
        refFrom[idx] = value
        refTo[idx] = copiedValue
        for key in value:
            copiedValue[key] = _clone(value[key], refFrom, refTo, True) if deep else value[key]
        return copiedValue
    if isinstance(value, dict): return copy({})
    if isinstance(value, list): return copy([])
    return value
