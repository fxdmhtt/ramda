# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .toString import toString

@_curry2
def test(pattern, str):
    # ignore: if _isRegExp
    import re
    return re.compile(pattern).search(str) is not None
