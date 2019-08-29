# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._toString import _toString

toString = _curry1(lambda val: _toString(val, []))
