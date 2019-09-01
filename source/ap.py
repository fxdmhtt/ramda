# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry2 import _curry2
from .internal._reduce import _reduce
from .map import map

@_curry2
def ap(applyF, applyX):
    from collections import Mapping
    return (
        # applyX['fantasy-land/ap'](applyF) if callable(applyX['fantasy-land/ap'])
        # else
        applyF.ap(applyX) if callable(getattr(applyF, 'ap', None))
        else applyF['ap'](applyX) if callable(isinstance(applyF, Mapping) and applyF.get('ap'))
        else (lambda x: applyF(x)(applyX(x))) if callable(applyF)
        else _reduce(lambda acc, f: _concat(acc, map(f, applyX)), [], applyF)
    )
