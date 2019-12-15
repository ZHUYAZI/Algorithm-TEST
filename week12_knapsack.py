#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:42:48 2019

@author: yazi
"""

import urllib.request
import numpy as np
target_url='https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack1.txt?Expires=1576540800&Signature=TaJu4rQIxNPAsnVeOm1rEedXov-EdYL0rUMEbqK~oRj4nD2OWzF0EpOXBSjkQn3LqvIYYkKThtz-lZott2RaiBLxBs9YLoQgTd7eMQj4nBAnzieLhn89J8pZCRpPgRJjWCPdF5rXaz-FcIcTyC3v-nlwEvGxLuXgbx5LVcrHQ7g_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
theArray=[]
number=0
n=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        knapsack_size,number_of_items=map(int,a.split(' '))
    else:
        theArray.append(list(map(int,a.split(' '))))

print(n)
#knapsack_size=6
#number_of_items=4
#theArray=[[3,4],[2,3],[4,2],[4,3]]
A=np.zeros((number_of_items+1,knapsack_size+1))
print(A.shape)
#initilize
A[0,:]=0
for i in range(1,number_of_items+1):
    for j in range(knapsack_size+1):
        if j>=theArray[i-1][1]:
            A[i,j]=max(A[i-1,j],A[i-1,j-theArray[i-1][1]]+theArray[i-1][0])
        else:
            A[i,j]=A[i-1,j]
            
print(A[-1,-1])