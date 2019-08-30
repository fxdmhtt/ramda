# -*- coding: utf-8 -*-

from .internal._clone import _clone
from .internal._curry1 import _curry1

@_curry1
def clone(value):
    return (
        value.clone() if value is not None and callable(getattr(value, 'clone', None))
        else _clone(value, [], [], True)
    )
