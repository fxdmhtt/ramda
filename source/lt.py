# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

from operator import lt
lt = _curry2(lt)
