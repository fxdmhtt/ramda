# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def uniqBy(fn, list):
    _set = set()
    for item in list:
        appliedItem = fn(item)
        if appliedItem not in _set:
            _set.add(appliedItem)
            yield item
