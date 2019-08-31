# -*- coding: utf-8 -*-

from ._arity import _arity
from ._curry2 import _curry2

from . import sig
from . import _apply, JSObject

def _createPartialApplicator(concat):
    from . import length
    return _curry2(lambda fn, args: \
        _arity(max(0, length(fn) - len(args)), sig(lambda *arguments: \
            _apply(fn, JSObject(), concat(args, arguments)))
        )
    )
