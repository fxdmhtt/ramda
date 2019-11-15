# -*- coding: utf-8 -*-

from .internal._objectIs import _objectIs
from .internal._curry2 import _curry2

identical = _curry2(_objectIs)
