# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def pickBy(test, obj):
    return {prop: obj[prop] for prop in obj if test(obj[prop], prop, obj)}
