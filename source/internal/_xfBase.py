# -*- coding: utf-8 -*-

from . import JSObject
_xfBase = JSObject({
    'init': lambda: \
        this.xf['@@transducer/init'](),
    'result': lambda result: \
        this.xf['@@transducer/result'](result)
})
