# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def evolve(transformations, object):
    result = [] if isinstance(object, (list, tuple)) else {}
    for key in object:
        transformation = transformations[key]
        result[key] = (
            transformation(object[key]) if callable(transformation)
            else evolve(transformation, object[key]) if transformation and isinstance(transformation, dict)
            else object[key]
        )
    return result
