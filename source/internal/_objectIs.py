# -*- coding: utf-8 -*-

def _objectIs(a, b):
    import math
    if isinstance(a, float) and math.isnan(a):
        return isinstance(b, float) and math.isnan(b)
    if isinstance(a, str) and isinstance(b, str):
        return a == b
    return id(a) == id(b)

    # ignore:

    # if a == b:
    #     return a != 0 or 1 / a == 1 / b
    # else:
    #     return a != a and b != b
