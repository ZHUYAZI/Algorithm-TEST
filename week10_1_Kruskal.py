#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:59:57 2019

@author: yazi
"""

import urllib.request
from collections import defaultdict
target_url='https://d3c33hcgiwev3.cloudfront.net/_fe8d0202cd20a808db6a4d5d06be62f4_clustering1.txt?Expires=1574380800&Signature=EF23uSW8KWPipplYg8wrsZDgBmhVsqVxicJeiG7fX79a9muuLvxpu5086h-rlIakZW1TqR4csLK38Ex6pGjq5bbvO75Aa6LFzxRjOBND181rOQ~9VCuzbRDA7FdJ8LUR-prz1IVxjDh-dTD6UWOLoBmW~Bo2A5AKcr378wRI~rI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
theArray=[]
node=0
n=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        node=int(a)
    else:
        n1,n2,l=a.split( )
        theArray.append([int(n1),int(n2),int(l)])

print(n)

theArray.sort(key=lambda x: x[2])

cluster= defaultdict(list)
pos=dict()

for i in range(node):
    cluster[i].append(i)
    pos[i]=i
    
while len(cluster)>4:  
    element=theArray.pop(0)
    if pos[element[0]-1] !=pos[element[1]-1]:
        #compare
        size1=len(cluster[pos[element[0]-1]])
        size2=len(cluster[pos[element[1]-1]])
        #renew
        if size1>=size2:
            cluster_del=pos[element[1]-1]
            cluster[pos[element[0]-1]]+=cluster[pos[element[1]-1]]
            for j in cluster[pos[element[1]-1]]:
                pos[j]=pos[element[0]-1]
            #merger
            del cluster[cluster_del]
            
        else:
            cluster_del=pos[element[0]-1]
            cluster[pos[element[1]-1]]+=cluster[pos[element[0]-1]]
            for j in cluster[pos[element[0]-1]]:
                pos[j]=pos[element[1]-1] 
                
            #merger
           
            del cluster[cluster_del]

print('distance =',theArray[0][2])      

