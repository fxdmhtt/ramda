# -*- coding: utf-8 -*-

from ._arity import _arity
from ._curry2 import _curry2

def _createPartialApplicator(concat):
    from . import getArgCount
    return _curry2(lambda fn, args: \
        _arity(max(0, getArgCount(fn) - len(args)), lambda *arguments: \
            fn(*concat(args, arguments))
        )
    )
