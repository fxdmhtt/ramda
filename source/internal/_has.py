# -*- coding: utf-8 -*-

def _has(prop, obj):
    from . import JSObject
    return hasattr(obj, prop) or isinstance(obj, JSObject) and prop in obj
