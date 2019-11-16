#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:31:47 2019

@author: yazi
"""

import urllib.request
from collections import defaultdict
target_url='https://d3c33hcgiwev3.cloudfront.net/_d4f3531eac1d289525141e95a2fea52f_edges.txt?Expires=1573862400&Signature=MDIB9uIEtSnAD6OLcGdmZ0JOdcHOGnxHij8-prRhz0JMlf~XVtz-7aopZHR5-UkHsjt~yh4Khi~kv5zPf9vXfkTfY8g55fYupaOUu7dt4UeNaz8WOZXHOEq6qRUaRZjRlVNoRs4TjXGlFWWxLuWIRviQO7pNsXZTBlyCPya1MQo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
n=0
theArray=defaultdict(dict)
node=0
edge=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        node,edge=a.split( )
    else:
        n1,n2,l=a.split( )
        theArray[int(n1)][int(n2)]=int(l)
        theArray[int(n2)][int(n1)]=int(l)

print(n)

import random


choice=random.randint(1, int(node))

v=[]
w={}
x=[]
v.append(choice)
w=theArray[choice]
sums=0
while len(v)<int(node):
    if len(w)==0:
        break
    choice,edge=min(w.items(), key=lambda x: x[1])
    x.append(edge)
    v.append(choice)
    sums+=edge
    w.pop(choice)
    for key,value in theArray[choice].items():
        if key not in v:
            length=w.get(key,float('inf'))
            length=min(length,value)
            w[key]=length

print(sums)
