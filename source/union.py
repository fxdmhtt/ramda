# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry2 import _curry2
from .compose import compose
from .uniq import uniq

union = _curry2(compose(uniq, _concat))
