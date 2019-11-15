# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._dropLastWhile import _dropLastWhile
from .internal._xdropLastWhile import _xdropLastWhile

dropLastWhile = _curry2(_dispatchable([], _xdropLastWhile, _dropLastWhile))
