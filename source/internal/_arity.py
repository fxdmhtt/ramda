# -*- coding: utf-8 -*-

def _arity(*arguments):
    n, fn, *_ = arguments
    if n == 0: return lambda: fn(*arguments)
    elif n == 1: return lambda a0: fn(*arguments)
    elif n == 2: return lambda a0, a1: fn(*arguments)
    elif n == 3: return lambda a0, a1, a2: fn(*arguments)
    elif n == 4: return lambda a0, a1, a2, a3: fn(*arguments)
    elif n == 5: return lambda a0, a1, a2, a3, a4: fn(*arguments)
    elif n == 6: return lambda a0, a1, a2, a3, a4, a5: fn(*arguments)
    elif n == 7: return lambda a0, a1, a2, a3, a4, a5, a6: fn(*arguments)
    elif n == 8: return lambda a0, a1, a2, a3, a4, a5, a6, a7: fn(*arguments)
    elif n == 9: return lambda a0, a1, a2, a3, a4, a5, a6, a7, a8: fn(*arguments)
    elif n == 10: return lambda a0, a1, a2, a3, a4, a5, a6, a7, a8, a9: fn(*arguments)
    else: raise ValueError('First argument to _arity must be a non-negative integer no greater than ten')
