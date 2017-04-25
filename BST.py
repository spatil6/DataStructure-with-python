# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:46:19 2017

@author: sandip
"""

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def BinaryInsert(root,data):
    if root is None:
        root=data
     #   print(data.data)
    else:
        if root.data > data.data:
            if root.left is None:
                root.left=data
        #        print(data.data)
            else:
                BinaryInsert(root.left,data)
        else:
            if root.right is None:
                root.right =data
       #         print(data.data)
            else:
                BinaryInsert(root.right,data)
def SearchNode(root,data):
    print(root.data)
    print(data.data)
    if root.data == data.data:
        return 'cor'
    if root.data < data.data:
        SearchNode(root.right,data)
    else:
        SearchNode(root.left,data)
        
def in_order_print(root):
    if not root:
        return
    in_order_print(root.left)
    print(root.data)
    in_order_print(root.right)
        
def pre_order_print(root):
    if not root:
        return        
    print(root.data)
    pre_order_print(root.left)
    pre_order_print(root.right)         


r = Node(3)

#BinaryInsert(None, Node(3))
BinaryInsert(r, Node(7))
BinaryInsert(r, Node(1))
BinaryInsert(r, Node(5))
in_order_print(r)

#print(SearchNode(r,Node(1)))
#pre_order_print(r)
    
