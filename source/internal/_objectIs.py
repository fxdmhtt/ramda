# -*- coding: utf-8 -*-

def _objectIs(a, b):
    if a == b:
        return a != 0 or 1 / a == 1 / b
    else:
        return a != a and b != b
