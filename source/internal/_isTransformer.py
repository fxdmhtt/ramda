# -*- coding: utf-8 -*-

def _isTransformer(obj):
    return obj is not None and callable(getattr(obj, '@@transducer/step'))
