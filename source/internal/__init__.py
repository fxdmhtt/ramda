# -*- coding: utf-8 -*-

class JSObject:
    def __init__(self, d):
        self.__dict__.update(d)

    def __getattr__(self, name):
        return None

class undefined(JSObject):
    def __init__(self):
        super().__init__({'@@functional/undefined': True})

    def __repr__(self):
        return 'undefined'

undefined = undefined()
