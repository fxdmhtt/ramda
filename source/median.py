# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .mean import mean

@_curry1
def median(list):
    len_ = len(list)
    if len_ == 0:
        return float('nan')
    width = 2 - len_ % 2
    idx = (len_ - width) / 2
    return mean(sorted(list[0:])[idx:idx + width])
