# -*- coding: utf-8 -*-

def _forceReduced(x):
    return {
        '@@transducer/value': x,
        '@@transducer/reduced': True
    }
