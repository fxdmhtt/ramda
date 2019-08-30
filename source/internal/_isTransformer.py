# -*- coding: utf-8 -*-

def _isTransformer(obj):
    from . import JSObject
    return obj is not None and isinstance(obj, JSObject) and callable(obj['@@transducer/step'])
