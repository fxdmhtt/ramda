# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry2 import _curry2

from .internal import jsify

def forEach(fn, list_):
    list(map(jsify(fn), list_))
    return list_
forEach = _curry2(_checkForMethod('forEach', forEach))
