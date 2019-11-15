# -*- coding: utf-8 -*-

from .internal._identity import _identity
from .chain import chain

unnest = chain(_identity)
