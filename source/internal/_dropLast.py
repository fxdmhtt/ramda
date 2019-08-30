# -*- coding: utf-8 -*-

from ..take import take

def dropLast(n, xs):
    return take(len(xs) - n if n < len(xs) else 0, xs)
