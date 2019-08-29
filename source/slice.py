# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry3 import _curry3

slice = _curry3(_checkForMethod('slice', lambda fromIndex, toIndex, list: list[fromIndex:toIndex]))
