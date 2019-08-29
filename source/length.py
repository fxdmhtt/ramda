# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isNumber import _isNumber

@_curry1
def length(list):
    from collections import Sized
    return list is not None and len(list) if isinstance(list, Sized) else float('nan')
