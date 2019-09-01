# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._dispatchable import _dispatchable
_xdropRepeatsWith = lambda x: x
from .dropRepeatsWith import dropRepeatsWith
from .equals import equals

dropRepeats = _curry1(
    _dispatchable([], _xdropRepeatsWith(equals), dropRepeatsWith(equals))
)
