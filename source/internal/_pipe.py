# -*- coding: utf-8 -*-

def _pipe(f, g):
    return lambda *arguments: g(f(*arguments))
