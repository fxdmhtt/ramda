# -*- coding: utf-8 -*-

from ._curry1 import _curry1
from ._isArray import _isArray
from ._isString import _isString

@_curry1
def _isArrayLike(x):
    if _isArray(x): return True
    if x is None: return False
    from collections import Collection
    if not isinstance(x, Collection): return False
    if _isString(x): return False
    if len(x) == 0: return True
    if len(x) > 0:
        return x.__getitem__(0) and x.__getitem__(len(x) - 1)
    return False
