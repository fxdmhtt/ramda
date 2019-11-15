# -*- coding: utf-8 -*-

from ._filter import _filter

def _functionsWith(fn):
    return lambda obj: \
        _filter(lambda key: callable(getattr(obj, key, None)), fn(obj))
