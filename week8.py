#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:17:31 2019

@author: yazi
"""

#import urllib.request
#target_url='https://d3c33hcgiwev3.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_algo1-programming_prob-2sum.txt?Expires=1573171200&Signature=TNe4hQj2ER1XqfRiTLLrD9QBtXq8qeaIFtuA9741U3TJfiTXYGcE1fZDmSWydCRhwc5RBNQUxXlGNdrR41fx9PjEKwqsspiF7g1xMPS5dwPUoZ9efT6LXYn6ftlLRTZ4lw~QQ6hYOekMTMYsbs3iG-lmgw1pX7V1Cn8BTuoSqyA_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
#file = urllib.request.urlopen(target_url)
#n=0
#data1=[]
#for line in file:
#    a=line.decode("utf-8").strip()
#    data1.append(int(a))
#    n+=1
#    
#print('n = ',n)
data1=[-3,-1,1,2,9,11,7,6,2]
data2=dict.fromkeys(data1,0)
num=[]
for i in range(3,11):
    print(i)
    for j in data1:
        aim=i-j
        if aim!=j:
            try:
                data2[aim]
                num.append((i,j,aim))
                break
            except:
                continue
        
print(len(num))     