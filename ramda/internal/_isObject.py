# -*- coding: utf-8 -*-

def _isObject(x):
    from collections import Mapping
    return isinstance(x, Mapping)
