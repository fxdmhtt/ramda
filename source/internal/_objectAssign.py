# -*- coding: utf-8 -*-

from ._has import _has

from . import sig

@sig(names=['target'])
def _objectAssign(*arguments):
    target, *_ = *arguments, None
    if target is None:
        raise TypeError('Cannot convert undefined or null to object')

    output = dict(target)
    idx = 1
    length = len(arguments)
    while idx < length:
        source = arguments[idx]
        if source is not None:
            for nextKey in source:
                if _has(nextKey, source):
                    output[nextKey] = source[nextKey]
        idx += 1
    return output
