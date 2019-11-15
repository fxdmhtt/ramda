# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def type(val):
    import builtins
    return (
        'None' if val is None
        else str(builtins.type(val))[8:-2]
    )
