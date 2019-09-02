# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._dispatchable import _dispatchable
from .internal._xdropRepeatsWith import _xdropRepeatsWith
from .dropRepeatsWith import dropRepeatsWith
from .equals import equals

dropRepeats = _curry1(
    _dispatchable([], _xdropRepeatsWith(equals), dropRepeatsWith(equals))
)
