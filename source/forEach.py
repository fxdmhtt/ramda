# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry2 import _curry2

def forEach(fn, list):
    len = len(list)
    idx = 0
    while idx < len:
        fn(list[idx])
        idx += 1
    return list
forEach = _curry2(_checkForMethod('forEach', forEach)
