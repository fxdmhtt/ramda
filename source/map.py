# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._map import _map
from .internal._reduce import _reduce
from .internal._xmap import _xmap
from .curryN import curryN
from .keys import keys

from .internal import sig
from .internal import length

@_curry2
def map(fn, functor):
    if callable(functor):
        return curryN(length(functor), sig(lambda *arguments: \
            fn(functor(*arguments)))
        )
    elif isinstance(functor, dict):
        return _reduce(lambda acc, key: \
            (
                acc.__setitem__(key, fn(functor[key])),
                acc
            )[-1]
        , {}, keys(functor))
    else:
        return _map(fn, functor)
map = _curry2(_dispatchable(['fantasy-land/map', 'map'], _xmap, map))
