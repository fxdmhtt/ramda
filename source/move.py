# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def move(from_, to, list):
    length = len(list)
    result = list[:]
    positiveFrom = (length + from_) if from_ < 0 else from_
    positiveTo = (length + to) if to < 0 else to
    item = result[positiveFrom:positiveFrom + 1]
    result = result[:positiveFrom] + result[positiveFrom + 1:]

    return (
        list if positiveFrom < 0 or positiveFrom >= len(list) \
             or positiveTo   < 0 or positiveTo   >= len(list)
        else result[:positiveTo] + item + result[positiveTo:]
    )
