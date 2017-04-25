# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:23:26 2017

@author: SP43190
"""

class BinaryTree:
    def __init__(self,root):
        self.left=None
        self.right=None
        self.data=root
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,data):
        self.data=data
    def getNodeValue(self):
        return self.data