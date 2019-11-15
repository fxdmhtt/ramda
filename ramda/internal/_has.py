# -*- coding: utf-8 -*-

def _has(prop, obj):
    from collections import Mapping, Collection
    return (
        isinstance(prop, str) and hasattr(obj, prop)
        or isinstance(obj, Mapping) and prop in obj
        or isinstance(prop, int) and isinstance(obj, Collection) and prop < len(obj)
    )
