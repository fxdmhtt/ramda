# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

add = _curry2(lambda a, b: a + b)
