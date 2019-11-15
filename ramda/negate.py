# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

from operator import neg
negate = _curry1(neg)
