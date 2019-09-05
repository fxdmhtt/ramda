# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .equals import equals
from .take import take

@_curry2
def startsWith(prefix, list):
    return (
        list.startswith(prefix) if isinstance(list, str)
        else equals(take(len(prefix), list), prefix)
    )
