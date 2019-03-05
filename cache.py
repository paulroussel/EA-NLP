# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:50:42 2019

@author: auges
"""

import pickle
import os

class Cache:
    CACHE = 'cache_dir/'
    MAINFILE = CACHE + 'mainfile.txt'

    def update(self,object_name):
        if not self.check(self.MAINFILE):
            with open(self.MAINFILE,'wb') as f:
                pickle.dump(obj=[object_name], file=f)
        else:
            l = self.get_list()
            if object_name not in l:
                l.append(object_name)
                with open(self.MAINFILE,'wb') as f:
                    pickle.dump(obj=l, file=f)

    def get_list(self):
        with open(self.MAINFILE,'rb') as f:
            return pickle.load(f)

    def check(self, name):
        return os.path.exists(self.CACHE + name)

    def load(self, name):
        with open(self.CACHE + name, 'rb') as f:
            return pickle.load(f)

    def save(self, obj, name):
        self.update(name)
        with open(self.CACHE + name, 'wb') as f:
            return pickle.dump(obj=obj, file=f)