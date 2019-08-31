# -*- coding: utf-8 -*-

from .curry import curry

from .internal import sig
from .internal import _apply, JSObject

@curry
@sig(names=['fn'])
def call(*arguments):
    fn, *_ = *arguments, None
    return _apply(fn, JSObject(), arguments[1:])
