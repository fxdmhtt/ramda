# -*- coding: utf-8 -*-

from collections import Mapping, Collection

def _getitem_from_collection(obj, idx):
    try:
        return obj[idx]
    except IndexError:
        return None

def _getitem(obj, prop):
    if isinstance(prop, str) and hasattr(obj, prop):
        return getattr(obj, prop)
    elif isinstance(obj, Mapping):
        return obj.get(prop)
    elif isinstance(prop, int):
        if isinstance(obj, (Collection, str)):
            return _getitem_from_collection(obj, prop)
