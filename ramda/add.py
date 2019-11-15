# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from operator import add
add = _curry2(add)
