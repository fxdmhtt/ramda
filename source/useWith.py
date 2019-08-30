# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .curryN import curryN

@_curry2
def useWith(fn, transformers):
    def function(*arguments):
        args = []
        idx = 0
        while idx < len(transformers):
            args.append(transformers[idx](arguments[idx]))
            idx += 1
        return fn(*(args + arguments[len(transformers):]))
    return curryN(len(transformers), function)
