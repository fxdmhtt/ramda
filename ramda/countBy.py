# -*- coding: utf-8 -*-

from .reduceBy import reduceBy

countBy = reduceBy(lambda acc, elem: acc + 1, 0)
