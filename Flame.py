# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 04:37:15 2019
@author: Ayush Jain
"""

def rml(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i]==l2[j]:
                c=l1[i]
                l1.remove(c)
                l2.remove(c)
                l=l1+["*"]+l2
                return [l,True]
    l=l1+["*"]+l2
    return [l,False]

p1 = input("Enter the first person name : ")
p1 = p1.lower()
p1 = p1.replace(" ","")
p2 = input("Enter the second person name : ")
p2 = p2.lower()
p2 = p2.replace(" ","")
l1=list(p1)
l2=list(p2)
proceed=True
while proceed:
    rl = rml(l1,l2)
    cl = rl[0]
    proceed = rl[1]
    si = cl.index('*')
    l1 = cl[:si]
    l2 = cl[si+1:]
    
c = len(l1)+len(l2)
r=["Friends","Love","Affection","Marriage","Enemy","Siblings"]

while len(r)>1:
    spi = (c%len(r))-1
    if spi>=0:
        ri = r[spi+1:]
        l = r[:spi]
        r = ri+l
    else:
        r = r[:len(r)-1]
        
print(r[0])
