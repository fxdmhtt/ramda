# -*- coding: utf-8 -*-

from .filter import filter
from .juxt import juxt
from .reject import reject

partition = juxt([filter, reject])
