# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._dropLast import _dropLast
_xdropLast = None

dropLast = _curry2(_dispatchable([], _xdropLast, _dropLast))
