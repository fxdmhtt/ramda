# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .pipeWith import pipeWith
from .reverse import reverse

@_curry2
def composeWith(xf, list_):
    return pipeWith(xf, list(reverse(list_)))
