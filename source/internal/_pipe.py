# -*- coding: utf-8 -*-

from . import sig

def _pipe(f, g):
    return sig(lambda *arguments: \
        g(f(*arguments)))
