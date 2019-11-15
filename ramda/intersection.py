# -*- coding: utf-8 -*-

from .internal._includes import _includes
from .internal._curry2 import _curry2
from .internal._filter import _filter
from .flip import flip
from .uniq import uniq

@_curry2
def intersection(list1, list2):
    if len(list1) > len(list2):
        lookupList = list1
        filteredList = list2
    else:
        lookupList = list2
        filteredList = list1
    return uniq(_filter(flip(_includes)(lookupList), filteredList))
