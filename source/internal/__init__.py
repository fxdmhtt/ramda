# -*- coding: utf-8 -*-

from collections import UserList
class Array(UserList):
    def __init__(self, *args):
        super().__init__(*args)

    def __setitem__(self, key, value):
        if len(self.data) <= key:
            self.data += [None] * (key - len(self.data) + 1)
        super().__setitem__(key, value)
del UserList

class Object(object):
    def __init__(self, d):
        self.__dict__.update(d)
