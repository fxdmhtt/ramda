# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def keys(obj):
    return [] if not isinstance(obj, dict) else obj.keys()
