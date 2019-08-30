# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    from ..__ import __
    return a is __

    # ignore:

    # from . import JSObject
    # return a is not None and \
    #     isinstance(a, JSObject) and \
    #     a['@@functional/placeholder'] == True
