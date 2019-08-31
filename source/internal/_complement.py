# -*- coding: utf-8 -*-

from . import sig
from . import _apply, JSObject

def _complement(f):
    return sig(lambda *arguments: \
        not _apply(f, JSObject(), arguments))
