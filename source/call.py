# -*- coding: utf-8 -*-

from .curry import curry

@curry
def call(fn, *args):
    return fn(*args)
