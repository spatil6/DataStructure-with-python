# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:42:09 2017

@author: SP43190
"""

class Stack:
    def __init__(self):
        self.container=[]
        
    def isEmpty(self):
        return self.size() == 0
    def push(self,item):
        self.container.append(item)
    def peek(self):
         return self.items[len(self.items)-1]        
    def pop(self):
        return self.container.pop()
    def size(self):
        return len(self.container)