# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .assoc import assoc
from .lens import lens
from .prop import prop

@_curry1
def lensProp(k):
    return lens(prop(k), assoc(k))
