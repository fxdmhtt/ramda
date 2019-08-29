# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry3 import _curry3
from .uniqWith import uniqWith

@_curry3
def unionWith(pred, list1, list2):
    return uniqWith(pred, _concat(list1, list2))
