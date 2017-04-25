# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 11:09:36 2017

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
        
class UnorderedList:

    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self,add):
        temp=Node(add)
        temp.setNext(self.head)
        self.head=temp
    def size(self):
        current=self.head
        count =0
        while current:
            count +=1
            current=current.getNext()
        return count
    def search(self,item):
        current=self.head
        isfount= False
        while current != None and not isfount:
            if current.getData()==item:
                isfount=True
            else:
                current=current.getNext
        return isfount
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    
            
        