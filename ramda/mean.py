# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .sum import sum

@_curry1
def mean(list):
    return sum(list) / len(list) if list else float('nan')
