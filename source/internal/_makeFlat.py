# -*- coding: utf-8 -*-

from ._isArrayLike import _isArrayLike

def _makeFlat(recursive):
    def flatt(list):
        value, jlen, j
        result = []
        idx = 0
        ilen = len(list)

        while idx < ilen:
            if _isArrayLike(list[idx]):
                value = flatt(list[idx]) if recursive else list[idx]
                j = 0
                jlen = len(value)
                while j < jlen:
                    result.append(value[j])
                    j += 1
            else:
                result.append(list[idx])
            idx += 1
        return result
    return flatt
