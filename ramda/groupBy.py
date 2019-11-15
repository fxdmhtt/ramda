# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry2 import _curry2
from .reduceBy import reduceBy

def function(acc, item):
    if acc is None:
        acc = []
    acc.append(item)
    return acc
groupBy = _curry2(_checkForMethod('groupBy', reduceBy(function, None)))
