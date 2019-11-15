# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .prop import prop
from .equals import equals

@_curry3
def propEq(name, val, obj):
    return equals(val, prop(name, obj))
