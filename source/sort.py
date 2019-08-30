# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def sort(comparator, list):
    from functools import cmp_to_key
    return sorted(list[0:], key=cmp_to_key(comparator))
