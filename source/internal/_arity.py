# -*- coding: utf-8 -*-

def _arity(n, fn):
    if n == 0: return lambda: fn()
    elif n == 1: return lambda a0: fn(a0)
    elif n == 2: return lambda a0, a1: fn(a0, a1)
    elif n == 3: return lambda a0, a1, a2: fn(a0, a1, a2)
    elif n == 4: return lambda a0, a1, a2, a3: fn(a0, a1, a2, a3)
    elif n == 5: return lambda a0, a1, a2, a3, a4: fn(a0, a1, a2, a3, a4)
    elif n == 6: return lambda a0, a1, a2, a3, a4, a5: fn(a0, a1, a2, a3, a4, a5)
    elif n == 7: return lambda a0, a1, a2, a3, a4, a5, a6: fn(a0, a1, a2, a3, a4, a5, a6)
    elif n == 8: return lambda a0, a1, a2, a3, a4, a5, a6, a7: fn(a0, a1, a2, a3, a4, a5, a6, a7)
    elif n == 9: return lambda a0, a1, a2, a3, a4, a5, a6, a7, a8: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
    elif n == 10: return lambda a0, a1, a2, a3, a4, a5, a6, a7, a8, a9: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
    else: raise ValueError('First argument to _arity must be a non-negative integer no greater than ten')
