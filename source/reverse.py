# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isString import _isString

@_curry1
def reverse(list_):
    return (
        ''.join(reversed(list_)) if _isString(list_)
        else list(reversed(list_[0:]))
    )
