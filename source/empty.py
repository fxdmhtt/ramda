# -*- coding: utf-8 -*-

from .internal._curry1 import _curry1
from .internal._isArray import _isArray
from .internal._isObject import _isObject
from .internal._isString import _isString

@_curry1
def empty(x):
    return (
        x['fantasy-land/empty']() if x is not None and callable(x['fantasy-land/empty'])
        else (
            x.constructor['fantasy-land/empty']() if x is not None and x.constructor is not None and callable(x.constructor['fantasy-land/empty'])
            else (
                x.empty() if x is not None and callable(getattr(x, 'empty', None))
                else (
                    x.constructor.empty() if x is not None and x.constructor is not None and callable(x.constructor.empty)
                    else (
                        [] if _isArray(x)
                        else '' if _isString(x)
                        else {} if _isObject(x)
                        else 0
                    )
                )
            )
        )
    )
