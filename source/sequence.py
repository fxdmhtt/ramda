# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .ap import ap
from .map import map
from .prepend import prepend
from .reduceRight import reduceRight

@_curry2
def sequence(of, traversable):
    return (
        traversable.sequence(of) if callable(traversable.sequence)
        else reduceRight(
            lambda x, acc: ap(map(prepend, x), acc),
            of([]),
            traversable
        )
    )
