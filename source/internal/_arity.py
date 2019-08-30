# -*- coding: utf-8 -*-

def _arity(n, fn):
    from . import defJSFunction
    if   n ==  0: return defJSFunction(lambda *arguments: fn(*arguments), [])
    elif n ==  1: return defJSFunction(lambda *arguments: fn(*arguments), ['a0'])
    elif n ==  2: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1'])
    elif n ==  3: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2'])
    elif n ==  4: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3'])
    elif n ==  5: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4'])
    elif n ==  6: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5'])
    elif n ==  7: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'])
    elif n ==  8: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'])
    elif n ==  9: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8'])
    elif n == 10: return defJSFunction(lambda *arguments: fn(*arguments), ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'])
    else: raise ValueError('First argument to _arity must be a non-negative integer no greater than ten')
