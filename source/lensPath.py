# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .assocPath import assocPath
from .lens import lens
from .path import path

@_curry1
def lensPath(p):
    return lens(path(p), assocPath(p))
