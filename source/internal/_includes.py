# -*- coding: utf-8 -*-

from ._indexOf import _indexOf

def _includes(a, list):
    return _indexOf(list, a, 0) >= 0
