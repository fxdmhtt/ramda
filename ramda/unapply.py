# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

from .internal import sig

@_curry1
def unapply(fn):
    return sig(lambda *arguments: \
        fn(arguments))
