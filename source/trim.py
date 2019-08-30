# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

# ignore: implementation

@_curry1
def trim(str):
    return str.strip()
