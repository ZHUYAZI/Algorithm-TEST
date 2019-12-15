#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:24:23 2019

@author: yazi
"""

import time
import urllib.request
target_url='https://d3c33hcgiwev3.cloudfront.net/_6dfda29c18c77fd14511ba8964c2e265_knapsack_big.txt?Expires=1576540800&Signature=S4BF9GrdJK7QWGZihxPGUf6vpSklxnVQehZFAtCZEWOSLDO2KHT~Xywd-a2khw422scakDmx7mWHouelUhFdg07q97Q29xs7SJt0-IJWElR8C9yYCphtgNbgJyaMKRcoesNYt15ND4otw3eqIFGWJxItrWwx0vqTiZCLECGIqYI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
theArray={}
number=0
n=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        knapsack_size,number_of_items=map(int,a.split(' '))
    else:
        theArray[number]=list(map(int,a.split(' ')))
        number+=1


table={}

def solve(n, w):
    if n==1:
        if w<theArray[n-1][1]:
            return 0
        else:
            return theArray[n-1][0]
    else:
        if (n,w) in table:
            return table[(n,w)]
        else:
            print(n,w)
            a1=solve(n-1, w)
            if w>theArray[n-1][1]:
                a2=solve(n-1, w-theArray[n-1][1])+theArray[n-1][0]
            else:
                a2=0
            result=max(a1,a2)
            table[(n,w)]=result
            return result



start=time.time()
max_value= solve(number_of_items, knapsack_size)
end=time.time()
print('max_value=',max_value,'time cost',-start+end,'s')
