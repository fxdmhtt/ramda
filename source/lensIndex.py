# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .lens import lens
from .nth import nth
from .update import update

@_curry1
def lensIndex(n):
    return lens(nth(n), update(n))
