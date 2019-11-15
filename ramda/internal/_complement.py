# -*- coding: utf-8 -*-

from . import sig

def _complement(f):
    return sig(lambda *arguments: \
        not f(*arguments))
