# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:20:18 2020

@author: Ayush Jain
"""

n = int(input('Number: '))
m = int(input('Number: '))
val = n
valn = m
a=""
while n!=0:
    if n%2==0:
        a = "0"+a
    else:
        a = "1"+a
    n = n//2
b=""
while m!=0:
    if m%2==0:
        b = "0"+b
    else:
        b = "1"+b
    m = m//2
print("\nBinary value of "+str(val)+" is "+a)
print("Binary Value of "+str(valn)+" is "+b)

v1 = a[::-1]
v2 = b[::-1]
s = ""
cs = 0
c = 0
for i in v1:
    try:
        a1 = int(v1[cs])
    except:
        a1=0
    try:
        a2 = int(v2[cs])
    except:
        a2 = 0
    d = (a1+a2+c) // 2
    s = str(a1+a2+c -(2*d))+s
    c = d
    cs +=1
s = str(c)+s
print("\nBinary Sum of "+a+" and "+ b+" is "+s)

v3=s[::-1]
o = 0
c = 0
for i in v3:
    if i=="1":
        o = o + pow(2,c)
    c+=1
print("Integer value of sum of "+str(val)+" and "+str(valn)+" is "+str(o))