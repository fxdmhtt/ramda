# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from operator import gt
gt = _curry2(gt)
