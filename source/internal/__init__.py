# -*- coding: utf-8 -*-

class JSObject:
    def __init__(self, d):
        self.__dict__.update(d)

undefined = JSObject({'@@functional/undefined': True})
