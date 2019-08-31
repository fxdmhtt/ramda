# -*- coding: utf-8 -*-

from .curryN import curryN
from .internal._curry1 import _curry1

from .internal import sig
from .internal import length

@_curry1
def thunkify(fn):
    @sig
    def createThunk(*arguments):
        fnArgs = arguments
        return sig(lambda *_: \
            fn(*fnArgs))
    return curryN(length(fn), createThunk)
