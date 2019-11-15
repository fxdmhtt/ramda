# -*- coding: utf-8 -*-

from ._curryN import _curryN
from ._has import _has
from ._xfBase import _xfBase

# ignore: XReduceBy

_xreduceBy = _curryN(4, [],
    lambda valueFn, valueAcc, keyFn, xf: \
        None
)
