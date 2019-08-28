# -*- coding: utf-8 -*-

import ._arity import _arity
import ._isPlaceholder import _isPlaceholder

def _curryN(length, received, fn):
    from functools import wraps
    from . import List
    @wraps(fn)
    def function(*arguments):
        combined = List()
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
            combined[combinedIdx] = result
            if not _isPlaceholder(result):
                left -= 1
            combinedIdx += 1
        return fn(*combined) if left <= 0 else _arity(left, _curryN(length, combined, fn))
    return function
