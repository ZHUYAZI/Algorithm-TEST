#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:03:56 2019

@author: yazi
"""

import urllib.request
from networkx.utils import UnionFind
from collections import defaultdict
from itertools import combinations
from operator import xor
target_url='https://d3c33hcgiwev3.cloudfront.net/_fe8d0202cd20a808db6a4d5d06be62f4_clustering_big.txt?Expires=1574467200&Signature=WB5FEW5u-ILXEoQMBktc~1~ABBCbg2UW8yiR0Q0OlVWgmoP2czz4YWDlHIrXY5bE5QCi8mezhE-0gs-6kK25eAIrMaC0nw7icI0hOE7bBlTssS8ZiAFziK2OPsbcOFHduY0WXwyAnx-cYhgNNbP8cVaahM56vNEosVdcvccKFtI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
theArray=[]
node=0
n_bits=0
n=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        node,n_bits=map(int,a.split())
    else:
        l=list(map(int,a.split( )))
        i=0
        sums=0
        for chiffre in l:
            sums+=chiffre*2**i
            i+=1
        theArray.append(sums)


n_a=defaultdict(list)
for i,j in enumerate(theArray):
    n_a[j].append(i)


#Create a UnionFind-instance with the nodes [0..n-1] 
Structure= UnionFind(range(node))
#create the bit-masks for Hamming distance 0
bit_mask0=[0]
#Create an array of bit-masks for the distances.
#Create bit-masks for Hamming distance 1 by shifting the 1-bit iteratively by 24 positions. 
bit_mask1=[1 << i for i in range(n_bits)]
#create the bit-masks for Hamming distance 2
bit_mask2=[]
for i in combinations(range(n_bits),2):
    bit_mask2.append(xor(1<<i[0],1<<i[1]))
    
bit_mask=bit_mask0+bit_mask1+bit_mask2


for distance in bit_mask:
    for key in n_a:
        p2=xor(key,distance)
        if p2==key:
            Structure.union(*n_a[key])
        if p2 !=key and p2 in n_a:
            Structure.union(*n_a[key],*n_a[p2])
            

print(len(list(Structure.to_sets())))

