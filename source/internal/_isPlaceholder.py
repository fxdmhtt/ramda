# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    from . import JSObject
    return a is not None and \
        isinstance(a, JSObject) and \
        getattr(a, '@@functional/placeholder') == True
