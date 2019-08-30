# -*- coding: utf-8 -*-

def _arity(n, fn):
    from .. import __
    if n == 0: return lambda: fn()
    elif n == 1: return lambda a0=__: fn(a0)
    elif n == 2: return lambda a0=__, a1=__: fn(a0, a1)
    elif n == 3: return lambda a0=__, a1=__, a2=__: fn(a0, a1, a2)
    elif n == 4: return lambda a0=__, a1=__, a2=__, a3=__: fn(a0, a1, a2, a3)
    elif n == 5: return lambda a0=__, a1=__, a2=__, a3=__, a4=__: fn(a0, a1, a2, a3, a4)
    elif n == 6: return lambda a0=__, a1=__, a2=__, a3=__, a4=__, a5=__: fn(a0, a1, a2, a3, a4, a5)
    elif n == 7: return lambda a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__: fn(a0, a1, a2, a3, a4, a5, a6)
    elif n == 8: return lambda a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__: fn(a0, a1, a2, a3, a4, a5, a6, a7)
    elif n == 9: return lambda a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__, a8=__: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8)
    elif n == 10: return lambda a0=__, a1=__, a2=__, a3=__, a4=__, a5=__, a6=__, a7=__, a8=__, a9=__: fn(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
    else: raise ValueError('First argument to _arity must be a non-negative integer no greater than ten')
