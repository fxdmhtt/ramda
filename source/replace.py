# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def replace(regex, replacement, str):
    import re
    return re.sub(regex, replacement, str)
