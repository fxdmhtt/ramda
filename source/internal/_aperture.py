# -*- coding: utf-8 -*-

def _aperture(n, list):
    idx = 0
    limit = len(list) - (n - 1)
    acc = []
    while idx < limit:
        acc.append(list[idx:idx + n])
        idx += 1
    return acc
