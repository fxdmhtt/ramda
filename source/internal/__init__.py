# -*- coding: utf-8 -*-

from collections import UserList

class List(UserList):
    def __init__(self, *args):
        super().__init__(*args)

    def __setitem__(self, key, value):
        if len(self.data) <= key:
            self.data += [None] * (key - len(self.data) + 1)
        super().__setitem__(key, value)

del UserList
