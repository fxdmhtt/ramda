# -*- coding: utf-8 -*-

from ._includes import _includes
from ._map import _map
from ._quote import _quote
from ..keys import keys
from ..reject import reject

def _toString(x, seen):
    # ignore: recur

    # ignore: mapPairs

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
        # ignore toString
        
        return str(x)
