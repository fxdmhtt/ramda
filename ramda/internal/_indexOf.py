# -*- coding: utf-8 -*-

from ..equals import equals

def _indexOf(list, a, idx):
    # ignore: IE9

    try:
        return list.index(a, idx)
    except ValueError:
        return -1
