# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .equals import equals
from .path import path

@_curry3
def pathEq(_path, val, obj):
    return equals(path(_path, obj), val)
