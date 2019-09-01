# -*- coding: utf-8 -*-

from .pipe import pipe
from .reverse import reverse

from .internal import sig

@sig
def compose(*arguments):
    if len(arguments) == 0:
        raise ValueError('compose requires at least one argument')
    return pipe(*reverse(arguments))
