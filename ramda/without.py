# -*- coding: utf-8 -*-

from .internal._includes import _includes
from .internal._curry2 import _curry2
from .flip import flip
from .reject import reject

@_curry2
def without(xs, list):
    return reject(flip(_includes)(xs), list)
