# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:27:09 2017

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
    def addList(self,first,second):
        temp=[]
        cry=0
       
        while first is not None or second is not None:
            frst =first
            secnd=second
            fa=0
            sa=0
            if frst is not None:
                fa=frst.getData()
            else:
                fa=0
            if secnd is not None:
                sa=secnd.getData()
            else:
                sa=0
            Sum=fa + sa +cry
            cry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            
            temp.append(Sum)
            if frst is not None:
                first=frst.getNext()
            if secnd is not None:
                second=secnd.getNext()
        return temp
  
      
linkList1=UnorderedList()
linkList2=UnorderedList()
firstNumber=32
seconNumber=123
f=str(firstNumber)
s=str(seconNumber)
for digit in f:
    linkList1.add(int(digit))
for digit1 in s:
    linkList2.add(int(digit1))
p=UnorderedList()
result=p.addList(linkList1.head,linkList2.head)
res=''
for i in reversed(result):
     res +=str(i)
print(res)

            
    
        