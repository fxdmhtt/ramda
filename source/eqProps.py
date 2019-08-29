# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .equals import equals

@_curry3
def eqProps(prop, obj1, obj2):
    return equals(obj1[prop], obj2[prop])
