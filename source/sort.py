# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from functools import cmp_to_key

@_curry2
def sort(comparator, list):
    return sorted(list, key=cmp_to_key(comparator))
