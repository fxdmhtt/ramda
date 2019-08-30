# -*- coding: utf-8 -*-

def _reduced(x):
    from . import JSObject
    return (
        x if x and x['@@transducer/reduced']
        else JSObject({
            '@@transducer/value': x,
            '@@transducer/reduced': True
        })
    )
