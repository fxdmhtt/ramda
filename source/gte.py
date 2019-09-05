# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from operator import ge
gte = _curry2(ge)
