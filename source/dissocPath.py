# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._isInteger import _isInteger
from .internal._isArray import _isArray
from .assoc import assoc
from .dissoc import dissoc
from .remove import remove
from .update import update

@_curry2
def dissocPath(path, obj):
    if len(path) == 0:
        return obj
    elif len(path) == 1:
        return remove(path[0], 1, obj) if _isInteger(path[0]) and _isArray(obj) else dissoc(path[0], obj)
    else:
        head = path[0]
        tail = path[1:]
        if obj[head] is None:
            return obj
        elif _isInteger(head) and _isArray(obj):
            return update(head, dissocPath(tail, obj[head]), obj)
        else:
            return assoc(head, dissocPath(tail, obj[head]), obj)
