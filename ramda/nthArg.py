# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .curryN import curryN
from .nth import nth

from .internal import sig

@_curry1
def nthArg(n):
    arity = 1 if n < 0 else n + 1
    return curryN(arity, lambda *arguments: \
        nth(n, arguments)
    )
