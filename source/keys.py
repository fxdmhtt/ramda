# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

# ignore: IE < 9

# ignore: Safari bug

# ignore: contains

@_curry1
def keys(obj):
    return [] if not isinstance(obj, dict) else list(obj.keys())

    # ignore: rest
