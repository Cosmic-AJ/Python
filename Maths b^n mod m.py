# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:52:47 2020

@author: Ayush Jain
"""
#b^n mod m

ba = power = 5 #value which needs to be raised
m = 11 #mod value
n = 178 #power

x = 1
val = n
a=""
b=""
while n!=0:
    if n%2==0:
        a = a+"0"
    else:
        a = a+"1"
    n = n//2
n = val
while n!=0:
    if n%2==0:
        b = "0"+b
    else:
        b = "1"+b
    n = n//2
print(str(ba)+"^"+str(val)+" mod "+str(m))
print("Binary Value for "+str(val)+" = "+b)

no = 0
for i in a:
    if i =="1":
        x = (x*power) % m
    power = (power*power) % m
    no = no+1
    if no!=len(a):
        print("Iteration: "+str(no)+" , x = "+str(x)+" power = "+str(power))
    else:
        print("Iteration: "+str(no)+", x = "+str(x))
print("Answer: "+str(x))