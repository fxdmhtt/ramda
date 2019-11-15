# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

import copy
from .internal._getitem import _getitem

@_curry1
def clone(value):
    cloneFn = _getitem(value, 'clone')
    return (
        cloneFn() if cloneFn
        else copy.deepcopy(value)
    )
