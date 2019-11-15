# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry2 import _curry2

@_curry2
def prepend(el, list):
    return _concat([el], list)
