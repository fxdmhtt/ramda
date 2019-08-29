# -*- coding: utf-8 -*-

def _complement(f):
    return lambda *arguments: not f(*arguments)
