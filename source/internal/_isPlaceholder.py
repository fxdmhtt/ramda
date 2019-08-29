# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    return a != None and \
        isinstance(a, dict) and \
        a.get('@@functional/placeholder') == True
