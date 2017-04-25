# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:48:38 2017

@author: SP43190
"""
from collections import deque

def palchecker(aString):
    chardeque = deque()

    for ch in aString:
        chardeque.appendleft(ch)

    stillEqual = True

    while len(chardeque) > 1 and stillEqual:
        first = chardeque.pop()
        last = chardeque.popleft()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker("radar"))
print(palchecker("rasdadfdar"))