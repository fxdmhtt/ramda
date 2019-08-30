# -*- coding: utf-8 -*-

from ..equals import equals

def _indexOf(list, a, idx):
    # ignore: IE9

    while idx < len(list):
        if equals(list[idx], a):
            return idx
        idx += 1
    return -1
