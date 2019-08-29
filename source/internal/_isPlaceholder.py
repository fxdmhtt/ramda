# -*- coding: utf-8 -*-

from . import Object

def _isPlaceholder(a):
    return a != None and \
        isinstance(a, Object) and \
        a.__dict__.get('@@functional/placeholder') == True
