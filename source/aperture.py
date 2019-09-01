# -*- coding: utf-8 -*-

from .internal._aperture import _aperture
from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xaperture = None

aperture = _curry2(_dispatchable([], _xaperture, _aperture))
