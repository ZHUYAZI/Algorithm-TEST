#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:51:39 2019

@author: yazi
"""

import urllib.request
#from collections import defaultdict
target_url='https://d3c33hcgiwev3.cloudfront.net/_eed1bd08e2fa58bbe94b24c06a20dcdb_huffman.txt?Expires=1575676800&Signature=UhEhH0j3JaxFS1gJqiRiJHPUfkhW0d3d8UaHI1cYW7wecT-T-48Rw08IUWqC5QwOpqeDHXGSCANPX9Pz870hh5J0cmC-0kz4vcer7yGPMsubbwumNAccmCP5auIn-CmqBE5ARV6V5~YMrZhSUyJV3gD-ipW-eDB4fBrHmwYyzdg_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
theArray=[]
number=0
n=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        number=int(a)
    else:
        theArray.append(int(a))

print(n)
#theArray=[3,2,6,8,2,6]

class Node():
    def __init__(self,name,key):
        self.left=None
        self.right=None
        self.name=name
        self.key=key

def merge(node1,node2):
    node3=Node(node1.name+node2.name,node1.key+node2.key)
    node3.left=node1
    node3.right=node2
    return node3

def search_depth(node,depth):
    if node.left==None:
        d.append(depth)
    else:
        depth+=1
        search_depth(node.left,depth)
        search_depth(node.right,depth)
        


#initialisation
tree=[]
for i in range(len(theArray)):
    tree.append(Node(str(i),theArray[i]))
    

#search 2 min and merge
for i in range(len(theArray)-1):
    min1=min(tree, key=lambda x: x.key)
    index1=tree.index(min1)
    node1=tree.pop(index1)
    min2=min(tree, key=lambda x: x.key)
    index2=tree.index(min2)
    node2=tree.pop(index2)
    node3=merge(node1,node2)
    tree.append(node3)

d=[]
search_depth(tree[0],0)
print(min(d))
print(max(d))


        
        
        