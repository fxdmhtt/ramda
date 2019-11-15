# -*- coding: utf-8 -*-

from .internal._map import _map
from .identity import identity
from .pickAll import pickAll
from .useWith import useWith

project = useWith(_map, [pickAll, identity])
