# -*- coding: utf-8 -*-

from .curryN import curryN
from .internal._curry1 import _curry1

@_curry1
def thunkify(fn):
    def createThunk(*arguments):
        fnArgs = arguments
        return lambda *_: \
            fn(*fnArgs)
    return curryN(fn.__code__.co_argcount, createThunk)
