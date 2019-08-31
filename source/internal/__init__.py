# -*- coding: utf-8 -*-

# JSObject

from collections import UserDict

class JSObject(UserDict):
    def __init__(self, initialdata=None):
        super().__init__(initialdata)

    def __getattr__(self, name):
        return self[name]

    def __getitem__(self, key):
        val = super().__getitem__(key)
        if callable(val):
            # 绑定 this
            return _bind(val, self)
        else:
            return val

    @property
    def prototype(self):
        return self.data

del UserDict

# JSObject

# JSFunction

def _apply(fn, this, args=()):
    import types
    if isinstance(fn, types.MethodType) and isinstance(getattr(fn, '__self__'), JSObject):
        fn = _bind(fn, this)
    return fn(*args)

def _call(fn, this, *args):
    return _apply(fn, this, args)

def _bind(fn, this):
    import types
    if isinstance(fn, types.MethodType):
        fn = fn.__func__

    if this is not None:
        return types.MethodType(fn, this)
    else:
        return fn

import inspect
from inspect import Parameter

def length(fn):
    if hasattr(fn, 'length'):
        return fn.length

    return len(inspect.signature(fn).parameters)

def sig(fn=None, *, names=[]):
    """设置类 js 方法的理论形参，实际形参一定是 *arguments"""

    if fn is None:
        from functools import partial
        return partial(sig, names=names)

    if hasattr(fn, 'length'):
        return fn

    # 要求被 sig 包装的 fn 的参数
    # 有且仅有一个 *arguments
    parameters = inspect.signature(fn).parameters
    assert len(parameters) == 1 and parameters.get('arguments') == Parameter('arguments', Parameter.VAR_POSITIONAL)

    parameters = [
        Parameter(name, Parameter.POSITIONAL_ONLY)
        for name in names
    ]
    length = len(parameters)

    fn.__signature__ = inspect.signature(fn).replace(parameters=parameters)
    fn.length = length

    return fn

def jsify(fn):
    """包装普通方法成为类 js 方法，调用时将使任意实参适配上形参"""

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
        if len(args) == length or var_length:
            return fn(*args)
        elif len(args) > length:
            return fn(*args[:length])
        else:
            return fn(*(args + (None,) * (length - len(args))))

    _JSFunction.__signature__ = sig.replace(parameters=parameters)
    _JSFunction.length = length

    return _JSFunction

# JSFunction


if __name__ == "__main__":
    # test JSObject

    def fn(self, *args):
        assert args == (1, 'a')
        return self

    o = JSObject({'func': fn, '@@test/func': fn, 'val': True})
    assert o.func(1, 'a') is o
    assert o['func'](1, 'a') is o
    assert o['@@test/func'](1, 'a') is o
    assert o.val
    assert o['val']

    fn = _bind(o.func, JSObject())
    assert fn(1, 'a') is not o
