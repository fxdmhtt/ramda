# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def move(from, to, list):
    length = len(list)
    result = list[:]
    positiveFrom = length + from if from < 0 else from
    positiveTo = length + to if to < 0 else to
    item = result[positiveFrom]
    result.remove(item)

    return (
        list
        if positiveFrom < 0 or positiveFrom >= len(list)
        or positiveTo   < 0 or positiveTo   >= len(list)
        else result[0:positiveTo] + [item] + result[positiveTo:len(list)]
    )
