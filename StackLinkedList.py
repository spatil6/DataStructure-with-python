# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:59:04 2017

@author: SP43190
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
        
class StackLinkedList:
    def __init__(self):
        self.head=None
    def push(self,item):
        node=Node(item)
        node.setNext(self.head)
        self.head=node
    def peek(self):
         return self.head.getData()  
    def pop(self):
        temp=self.head.getData()
        self.head=self.head.getNext
        return temp
    def size(self):
        current=self.head
        count =0
        while current:
            count +=1
            current=current.getNext()
        return count