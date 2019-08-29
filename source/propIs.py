# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .is_ import is_

@_curry3
def propIs(type, name, obj):
    return is_(type, obj[name])
