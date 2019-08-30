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
    if x.get('length') == 0: return True
    if x.get('length', -1) > 0:
        return 0 in x and (x.get('length') - 1) in x
    return False
