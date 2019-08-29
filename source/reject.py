# -*- coding: utf-8 -*-

from .internal._complement import _complement
from .internal._curry2 import _curry2
from .filter import filter

@_curry2
def reject(pred, filterable):
    return filter(_complement(pred), filterable)
