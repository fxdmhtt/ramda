# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .concat import concat
from .difference import difference

@_curry2
def symmetricDifference(list1, list2):
    return concat(difference(list1, list2), difference(list2, list1))
