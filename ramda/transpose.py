# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1

@_curry1
def transpose(outerlist):
    i = 0
    result = []
    while i < len(outerlist):
        innerlist = outerlist[i]
        j = 0
        while j < len(innerlist):
            if j >= len(result):
                result.append([])
            result[j].append(innerlist[j])
            j += 1
        i += 1
    return result
