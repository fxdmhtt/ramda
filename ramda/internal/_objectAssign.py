# -*- coding: utf-8 -*-

from ._has import _has

from . import sig

@sig(names=['target'])
def _objectAssign(*arguments):
    target, *_ = *arguments, None
    if target is None:
        raise TypeError('Cannot convert undefined or null to object')

    output = dict(target)
    list(map(output.update, arguments[1:]))
    return output
