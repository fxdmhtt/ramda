# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._createPartialApplicator import _createPartialApplicator
from .flip import flip

partialRight = _createPartialApplicator(flip(_concat))
