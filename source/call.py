# -*- coding: utf-8 -*-

from .curry import curry

@curry
def call(*arguments):
    fn, *_ = arguments
    return fn(*arguments[1:])
