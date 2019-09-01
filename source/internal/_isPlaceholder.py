# -*- coding: utf-8 -*-

def _isPlaceholder(a):
    from ..__ import __
    return a is __

    # ignore:

    # return a is not None and \
    #     isinstance(a, dict) and \
    #     a['@@functional/placeholder'] == True
