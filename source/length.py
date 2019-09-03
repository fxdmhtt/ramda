# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isNumber import _isNumber

@_curry1
def length(list):
    if callable(list):
        from .internal import length
        return length(list)

    from collections import Sized, Mapping
    if isinstance(list, Mapping):
        import numbers
        if isinstance(list.get('length'), numbers.Number):
            return list['length']
    elif isinstance(list, Sized):
        return len(list)

    return float('nan')
