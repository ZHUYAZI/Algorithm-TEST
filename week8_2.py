#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:51:58 2019

@author: yazi
"""
import urllib.request
target_url='https://d3c33hcgiwev3.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1573171200&Signature=TNe4hQj2ER1XqfRiTLLrD9QBtXq8qeaIFtuA9741U3TJfiTXYGcE1fZDmSWydCRhwc5RBNQUxXlGNdrR41fx9PjEKwqsspiF7g1xMPS5dwPUoZ9efT6LXYn6ftlLRTZ4lw~QQ6hYOekMTMYsbs3iG-lmgw1pX7V1Cn8BTuoSqyA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
n=0
theArray=[]
for line in file:
    a=line.decode("utf-8").strip()
    theArray.append(int(a))
    n+=1
    
print('n = ',n)

theArray.sort()
theSums={}
theLo=0
theHi=len(theArray)-1
T1=10000
T2=-10000

while theHi>theLo:
    if theArray[theLo] + theArray[theHi]>T1:
        theHi-=1
        continue
    if theArray[theLo] + theArray[theHi]<T2:
        theLo+=1
        continue
    if theArray[theLo] == theArray[theHi]:
        break       
    theInLo=theLo
    sum1 = theArray[theInLo] + theArray[theHi]
    while sum1 >= T2 and sum1 <= T1:
        theSums[sum1]=0
        theInLo+=1
        if theArray[theHi] == theArray[theInLo]:
            break
        sum1 = theArray[theInLo] + theArray[theHi]
    theHi-=1
    
print(len(theSums))