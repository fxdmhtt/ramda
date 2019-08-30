# -*- coding: utf-8 -*-

from . import Object
_xfBase = Object({
    'init': lambda: \
        this.xf['@@transducer/init'](),
    'result': lambda result: \
        this.xf['@@transducer/result'](result)
})
