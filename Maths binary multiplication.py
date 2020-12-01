# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:40:34 2020

@author: Ayush Jain
"""
import sys

def add(a,b):
    v1 = a[::-1]
    v2 = b[::-1]
    s = ""
    cs = 0
    c = 0
    if len(v1)<len(v2):
        t = v1
        v1 = v2
        v2 = t
    
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
    return s

def multiply(a,b):
    v1 = a
    v2 = b
    p = ""
    cs = 0
    if len(v1)<=len(v2):
            t = v1
            v1 = v2
            v2 = t
    v1 = v1
    v2 = v2[::-1]
    for i in v1:
        try:
            if v2[cs] == "0":
                c = "0"
            else:
                c = v1
                su = "0"*cs
                c = c +su
        except:
            break
        p = add(p,c)
        cs+=1
    return p

print("+----------------------+")
print("| Enter 1 for integer  |")
print("| Enter 2 for binary   |")
print("+----------------------+",end='')
ans = int(input("Enter your choice: "))
if ans == 1:
    n = int(input('Enter number 1: '))
    m = int(input('Enter number 2: '))
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
elif ans==2:
    a = input('Enter number 1 in binary: ')
    b = input('Enter number 2 in binary: ')
    
    v3=a[::-1]
    o = 0
    c = 0
    for i in v3:
        if i=="1":
            o = o + pow(2,c)
        c+=1
    val = o
    
    v3=b[::-1]
    o = 0
    c = 0
    for i in v3:
        if i=="1":
            o = o + pow(2,c)
        c+=1
    valn = o
else:
    sys.exit()
    
p = multiply(a, b)
print("\nMultiplication of "+a+" and "+ b+" is "+p)

v3=p[::-1]
o = 0
c = 0
for i in v3:
    if i=="1":
        o = o + pow(2,c)
    c+=1
print("Integer multiplication of "+str(val)+" and "+str(valn)+" is "+str(o))