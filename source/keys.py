# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

# ignore: IE < 9

# ignore: Safari bug

# ignore: contains

@_curry1
def keys(obj):
    from collections import Mapping, Collection
    return list(
        [] if isinstance(obj, str)
        else obj.keys() if isinstance(obj, Mapping)
        else range(len(obj)) if isinstance(obj, Collection)
        else []
    )

    # ignore: rest
