# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def remove(start, count, list):
    return list[:start] + list[start + count:]
