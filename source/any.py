# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xany = None

def any(fn, list):
    idx = 0
    while idx < len(list):
        if fn(list[idx]):
            return True
        idx += 1
    return False
any = _curry2(_dispatchable(['any'], _xany, any))
