# -*- coding: utf-8 -*-

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

def getArgCount(fn):
    if hasattr(fn, 'length'):
        return fn.length

    import inspect
    return len(inspect.signature(fn).parameters)

def defJSFunction(fn, names):
    if hasattr(fn, 'length'):
        return fn

    import inspect
    fn.__signature__ = inspect.signature(fn).replace(parameters=[
        inspect.Parameter(name, inspect.Parameter.POSITIONAL_ONLY)
        for name in names
    ])
    fn.length = len(names)

    return fn

def wrapToJSFunction(fn):
    if hasattr(fn, 'length'):
        return fn

    import inspect
    sig = inspect.signature(fn)

    parameters = []
    length = 0
    var_length = False  # 支持变长参数
    for parameter in sig.parameters.values():
        if parameter.kind is inspect.Parameter.POSITIONAL_ONLY \
        or parameter.kind is inspect.Parameter.POSITIONAL_OR_KEYWORD:
            parameters.append(parameter)
            length += 1
        elif parameter.kind is inspect.Parameter.VAR_POSITIONAL:
            parameters.append(parameter)
            var_length = True
        elif parameter.kind is inspect.Parameter.KEYWORD_ONLY:
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
