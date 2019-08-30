# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._reduced import _reduced

reduced = _curry1(_reduced)
