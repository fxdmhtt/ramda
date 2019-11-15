# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

import re

@_curry3
def replace(regex, replacement, str):
    return re.sub(regex, replacement, str)
