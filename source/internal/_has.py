# -*- coding: utf-8 -*-

def _has(prop, obj):
    from collections import Mapping
    return isinstance(prop, str) and hasattr(obj, prop) or isinstance(obj, Mapping) and prop in obj
