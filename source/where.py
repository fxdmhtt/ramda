# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._has import _has

@_curry2
def where(spec, testObj):
    for prop in spec:
        if _has(prop, spec) and not spec[prop](testObj[prop]):
            return False
    return True
