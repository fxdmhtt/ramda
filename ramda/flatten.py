# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._makeFlat import _makeFlat

flatten = _curry1(_makeFlat(True))
