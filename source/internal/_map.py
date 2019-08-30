# -*- coding: utf-8 -*-

def _map(fn, functor):
    idx = 0
    len = len(functor)
    result = []
    while idx < len:
        result.append(fn(functor[idx]))
        idx += 1
    return result
