# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

from operator import not_
not_ = _curry1(not_)
