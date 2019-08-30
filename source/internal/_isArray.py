# -*- coding: utf-8 -*-

def _isArray(val):
    from collections import Collection, Mapping
    return isinstance(val, Collection) and not isinstance(val, (Mapping, str))
