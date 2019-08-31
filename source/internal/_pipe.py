# -*- coding: utf-8 -*-

from . import sig

from . import _call, _apply, JSObject

def _pipe(f, g):
    return sig(lambda *arguments: \
        _call(g, JSObject(), _apply(f, JSObject(), arguments)))
