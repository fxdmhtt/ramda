# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    from . import Object
    return a is not None and \
        isinstance(a, Object) and \
        getattr(a, '@@functional/placeholder') == True
