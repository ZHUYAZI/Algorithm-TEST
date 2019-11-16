#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 20:40:46 2019

@author: yazi

"""
import operator
tache=[]
n=0
with open('/home/yazi/Downloads/jobs.txt', 'r') as f:
    n=0
    for line in f:
        n+=1
        a,b=list(map(int, line.strip().split(" ")))
        tache.append([a/b,a,b])

print(n)
#tache= [[8/50,8,50], [74/59,74,59], [31/73,31,73],[45/79,45,79],[24/10,24,10],
#        [41/66,41,66],[93/43,93,43],[88/4,88,4],[28/30,28,30],[41/13,41,13],[4/70,4,70],[10/58,10,58] ] 
##w/l,w,l
tache.sort(key=operator.itemgetter(0,1),reverse=True)  
sums=0
days=0
for element in tache:
   days+=element[2]
   sums+=days*element[1]

