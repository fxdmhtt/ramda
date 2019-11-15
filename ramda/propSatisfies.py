# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .prop import prop

@_curry3
def propSatisfies(pred, name, obj):
    return pred(prop(name, obj))
