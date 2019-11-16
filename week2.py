#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:27:16 2019

@author: yazi
"""

import time
    
class count_inversion():
    def __init__(self,in_data):
        self.number_inversion=self.count(in_data)
        
    def count(self,data):
        
        if len(data)==1:
            return 0
        else:
            data1=data[0:len(data)//2]
            data2=data[len(data)//2:len(data)]
            num1=self.count(data1)+self.count(data2)+self.countsplit(data1,data2)
           
            return(num1)
       
    def countsplit(self,data1,data2):
        num=0
        for i in range(len(data1)):
            for j in range(len(data2)):
                if data1[i]>data2[j]:
                    num+=1
        
        return(num)
      
        

if __name__=='__main__':
    start=time.time()
    import urllib.request
    target_url='https://d3c33hcgiwev3.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1569542400&Signature=EiGJq74pfOp2QgTndOu~XOuUewF5iHWFuV~KajWAEnSKCy9uE6wcaOnIi8Q4rLZXxHyxJAKHqL3qG-Ioo~sT9FSBdHc773FRgwgjvK-vlvi395SoQwX~8Vs5bBt~55GgD1up~-ChnEiFDqQJXdPM7xHhaVnc4UvWC1MWrnZHbh4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
    file = urllib.request.urlopen(target_url)
    data=[]
    for line in file:
        a=line.decode("utf-8")
        data.append(int(a.strip()))
        
    result=count_inversion(data)
    print(result.number_inversion)     
    
#    test=[6,1,2,3,4,5]
#    result=count_inversion(test)
#    print(result.number_inversion)
    end=time.time()
    print('time cost = ', end-start,'  sec ')
    #389 sec