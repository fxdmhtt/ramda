# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .internal._reduce import _reduce

reduce = _curry3(_reduce)
