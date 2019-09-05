# -*- coding: utf-8 -*-

from .internal._checkForMethod import _checkForMethod
from .internal._curry1 import _curry1
from .slice import slice

tail = _curry1(_checkForMethod('tail', slice(1, None)))
