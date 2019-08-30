# -*- coding: utf-8 -*-

from ._curry2 import _curry2
from ._flatCat import _flatCat
from ..map import map

@_curry2
def _xchain(f, xf):
    return map(f, _flatCat(xf))
