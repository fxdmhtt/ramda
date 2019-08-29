# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .concat import concat
from .differenceWith import differenceWith

@_curry3
def symmetricDifferenceWith(pred, list1, list2):
    return concat(differenceWith(pred, list1, list2), differenceWith(pred, list2, list1))
