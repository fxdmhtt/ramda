# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._map import _map
from .internal._reduce import _reduce
from .internal._xmap import _xmap
from .curryN import curryN
from .keys import keys

from .internal import length

@_curry2
def map(fn, functor):
    if callable(functor):
        return curryN(length(functor), lambda *arguments: \
            fn(functor(*arguments))
        )
    elif isinstance(functor, dict):
        return {k: fn(functor[k]) for k in functor}
    else:
        return _map(fn, functor)
map = _curry2(_dispatchable(['map'], _xmap, map))
