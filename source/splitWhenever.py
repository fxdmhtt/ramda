# -*- coding: utf-8 -*-

from .internal._curryN import _curryN

def splitWhenever(pred, list):
    acc = []
    curr = []
    for i in range(len(list)):
        if not pred(list[i]):
            curr.append(list[i])
        if (i < len(list) - 1 and pred(list[i + 1]) or i == len(list) - 1) and len(curr) > 0:
            acc.append(curr)
            curr = []
    return acc
splitWhenever = _curryN(2, [], splitWhenever)
