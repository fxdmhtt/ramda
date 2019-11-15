# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

import re

@_curry2
def match(rx, str):
    return re.findall(rx, str) or []
