# -*- coding: utf-8 -*-

from .internal._includesWith import _includesWith
from .internal._curry2 import _curry2

@_curry2
def uniqWith(pred, list):
    result = []
    for item in list:
        if not _includesWith(pred, item, result):
            result.append(item)
            yield item
