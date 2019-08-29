# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def match(rx, str):
    import re
    return re.findall(rx, str) or []
