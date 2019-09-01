# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xall = None

def all(fn, list):
    idx = 0
    while idx < len(list):
        if not fn(list[idx]):
            return False
        idx += 1
    return True
all = _curry2(_dispatchable(['all'], _xall, all))
