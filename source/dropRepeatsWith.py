# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xdropRepeatsWith = None
from .last import last

def dropRepeatsWith(pred, list):
    result =[]
    idx = 1
    len_ = len(list)
    if len_ != 0:
        result[0] = list[0]
        while idx < len_:
            if not pred(last(result), list[idx]):
                result.append(list[idx])
            idx += 1
    return result
dropRepeatsWith = _curry2(_dispatchable([], _xdropRepeatsWith, dropRepeatsWith))
