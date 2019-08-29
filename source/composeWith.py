# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .pipeWith import pipeWith
from .reverse import reverse

def composeWith(xf, list):
    return pipeWith(*[xf, reverse(list)])
