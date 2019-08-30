# -*- coding: utf-8 -*-

def _includesWith(pred, x, list):
    idx = 0
    len_ = len(list)

    while idx < len_:
        if pred(x, list[idx]):
            return True
        idx += 1
    return False
