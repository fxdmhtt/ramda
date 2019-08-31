# -*- coding: utf-8 -*-

# JSObject

from collections import UserDict

class JSObject(UserDict):
    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def __getattr__(self, name):
        return self[name]

    @property
    def prototype(self):
        return self.data

del UserDict

# JSObject

# JSFunction

import inspect
from inspect import Parameter

def length(fn):
    if hasattr(fn, 'length'):
        return fn.length

    return len(inspect.signature(fn).parameters)

def sig(fn=None, *, names=[]):
    if fn is None:
        from functools import partial
        return partial(sig, names=names)

    if hasattr(fn, 'length'):
        return fn

    parameters = [
        Parameter(name, Parameter.POSITIONAL_ONLY)
        for name in names
    ]
    length = len(parameters)

    fn.__signature__ = inspect.signature(fn).replace(parameters=parameters)
    fn.length = length

    return fn

def jsify(fn):
    if hasattr(fn, 'length'):
        return fn

    sig = inspect.signature(fn)

    parameters = []
    length = 0
    var_length = False  # 支持变长参数
    for parameter in sig.parameters.values():
        if parameter.kind is Parameter.POSITIONAL_ONLY \
        or parameter.kind is Parameter.POSITIONAL_OR_KEYWORD:
            parameters.append(parameter)
            length += 1
        elif parameter.kind is Parameter.VAR_POSITIONAL:
            parameters.append(parameter)
            var_length = True
        elif parameter.kind is Parameter.KEYWORD_ONLY:
            raise ValueError('Unsupported function')

    from functools import wraps
    @wraps(fn)
    def _JSFunction(*args):
        if len(args) <= length or var_length:
            return fn(*args)
        else:
            return fn(*args[:length])

    _JSFunction.__signature__ = sig.replace(parameters=parameters)
    _JSFunction.length = length

    return _JSFunction

# JSFunction
