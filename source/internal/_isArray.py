# -*- coding: utf-8 -*-

def _isArray(val):
    from collections import Collection
    return isinstance(val, Collection)
