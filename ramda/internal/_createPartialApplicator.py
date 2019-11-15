# -*- coding: utf-8 -*-

from ._arity import _arity
from ._curry2 import _curry2

from . import sig

def _createPartialApplicator(concat):
    from . import length
    return _curry2(lambda fn, args: \
        _arity(max(0, length(fn) - len(args)), sig(lambda *arguments: \
            fn(*concat(args, arguments)))
        )
    )
