# -*- coding: utf-8 -*-

from .curry import curry

from .internal import sig

@curry
@sig(names=['fn'])
def call(*arguments):
    fn, *_ = *arguments, None
    return fn(*arguments[1:])
