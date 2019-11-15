# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._identity import _identity

identity = _curry1(_identity)
