# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 08:27:56 2020

@author: Ayush Jain
"""

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
x=0
if n1>n2:
    x = n1
    y = n2
else:
    x = n2
    y = n1

ans = 0
i = 1
while y!=0:
    r = x%y
    x = y
    y = r
    print("Iteration ",i,": ",y)
    i+=1
    if y!=0:
        ans = y
print("\ngcd(",n1,",",n2,") :",ans)