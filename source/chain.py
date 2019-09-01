# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._makeFlat import _makeFlat
_xchain = None
from .map import map

def chain(fn, monad):
    if callable(monad):
        return lambda x: fn(monad(x))(x)
    return _makeFlat(false)(map(fn, monad))
chain = _curry2(_dispatchable(['fantasy-land/chain', 'chain'], _xchain, chain))
