# -*- coding: utf-8 -*-

def _reduced(x):
    return (
        x if x and x['@@transducer/reduced']
        else {
            '@@transducer/value': x,
            '@@transducer/reduced': True
        }
    )
