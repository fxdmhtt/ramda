# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .equals import equals
from .map import map
from .where import where

@_curry2
def whereEq(spec, testObj):
    return where(map(equals, spec), testObj)
