# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._filter import _filter
from .internal._isObject import _isObject
from .internal._reduce import _reduce
from .internal._xfilter import _xfilter
from .keys import keys

def filter(pred, filterable):
    def function(acc, key):
        if pred(filterable[key]):
            acc[key] = filterable[key]
        return acc
    return (
        _reduce(function, {}, keys(filterable)) if _isObject(filterable)
        else _filter(pred, filterable)
    )
filter = _curry2(_dispatchable(['filter'], _xfilter, filter))
