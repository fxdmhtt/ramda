# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    return a is not None and \
        isinstance(a, dict) and \
        a.get('@@functional/placeholder') == True
