# -*- coding: utf-8 -*-

from ._includes import _includes
from ._map import _map
from ._quote import _quote
from ..keys import keys
from ..reject import reject

def _toString(x, seen):
    def recur(y):
        xs = seen.append(x)
        return '<Circular>' if _includes(y, xs) else _toString(y, xs)

    def mapPairs(obj, keys):
        return _map(lambda k: _quote(k) + ': ' + recur(obj[k]), sorted(keys[:]))

    import datetime
    import numbers
    if isinstance(x, (list, tuple)):
        return repr(x)
    elif isinstance(x, bool):
        return repr(x)
    elif isinstance(x, (datetime.datetime, datetime.date, datetime.time, datetime.timedelta)):
        return repr(x)
    elif x is None:
        return repr(x)
    elif isinstance(x, numbers.Number):
        return repr(x)
    elif isinstance(x, str):
        return repr(x)
    else:
        if callable(getattr(x, '__str__', None)):
            repr_ = x.__str__()
            return repr_
        return '{' + ', '.join(mapPairs(x, keys(x))) + '}'
