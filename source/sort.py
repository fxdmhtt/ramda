# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def sort(comparator, list):
    return sorted(list[0:], key=comparator)
