# -*- coding: utf-8 -*-

from ._has import _has

def _isArguments(x):
    return _has('callee', x)
