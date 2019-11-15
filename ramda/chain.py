# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._makeFlat import _makeFlat
from .internal._xchain import _xchain
from .map import map

def chain(fn, monad):
    if callable(monad):
        return lambda x: fn(monad(x))(x)
    return _makeFlat(False)(map(fn, monad))
chain = _curry2(_dispatchable(['chain'], _xchain, chain))
