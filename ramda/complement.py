# -*- coding: utf-8 -*-

from .lift import lift
from .not_ import not_

complement = lift(not_)
