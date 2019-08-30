# -*- coding: utf-8 -*-

from ._arrayFromIterator import _arrayFromIterator
from ._includesWith import _includesWith
from ._functionName import _functionName
from ._has import _has
from ._objectIs import _objectIs
from ..keys import keys
from ..type import type

def _uniqContentEquals(aIterator, bIterator, stackA, stackB):
    a = _arrayFromIterator(aIterator)
    b = _arrayFromIterator(bIterator)

    def eq(_a, _b):
        return _equals(_a, _b, stackA[:], stackB[:])

    return not _includesWith(lambda b, aItem: \
        not _includesWith(eq, aItem, b)
    , b, a)

def _equals(a, b, stackA, stackB):
    if _objectIs(a, b):
        return True

    typeA = type(a)

    if typeA != type(b):
        return False

    # ignore: fantasy-land/equals

    return a == b

    # ignore: rest
