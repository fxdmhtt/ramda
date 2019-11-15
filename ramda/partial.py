# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._createPartialApplicator import _createPartialApplicator

partial = _createPartialApplicator(_concat)
