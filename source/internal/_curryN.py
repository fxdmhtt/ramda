# -*- coding: utf-8 -*-

from ._arity import _arity
from ._isPlaceholder import _isPlaceholder

from . import sig

def _curryN(length, received, fn):
    from functools import wraps
    @wraps(fn)
    @sig
    def function(*arguments):
        combined = []
        argsIdx = 0
        left = length
        combinedIdx = 0
        while combinedIdx < len(received) or argsIdx < len(arguments):
            if combinedIdx < len(received) and \
                    (not _isPlaceholder(received[combinedIdx]) or \
                    argsIdx >= len(arguments)):
                result = received[combinedIdx]
            else:
                result = arguments[argsIdx]
                argsIdx += 1
            combined.append(result)
            if not _isPlaceholder(result):
                left -= 1
            combinedIdx += 1
        return (
            fn(*combined) if left <= 0
            else _arity(left, _curryN(length, combined, fn))
        )
    return function
