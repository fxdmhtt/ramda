# -*- coding: utf-8 -*-

def _filter(fn, list):
    idx = 0
    len_ = len(list)
    result = []

    while idx < len_:
        if fn(list[idx]):
            result.append(list[idx])
        idx += 1
    return result
