# -*- coding: utf-8 -*-

def _filter(fn, list):
    idx = 0
    len = len(list)
    result = []

    while idx < len:
        if fn(list[idx]):
            result.append(list[idx])
        idx += 1
    return result
