# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .pipeWith import pipeWith
from .reverse import reverse

from .internal import _apply, JSObject

def composeWith(xf, list):
    return _apply(pipeWith, JSObject(), [xf, reverse(list)])
