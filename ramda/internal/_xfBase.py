# -*- coding: utf-8 -*-

_xfBase = {
    'init': lambda: \
        this.xf['@@transducer/init'](),
    'result': lambda result: \
        this.xf['@@transducer/result'](result)
}
