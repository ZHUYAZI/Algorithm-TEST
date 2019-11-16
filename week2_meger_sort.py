#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:11:20 2019

@author: yazi
"""

import time
    
class merge_sort():
    def __init__(self,in_data):
        self.result=self.sort(in_data)
        
        
    def split(self,data):
        data1=data[0:len(data)//2]
        data2=data[len(data)//2:len(data)]
        return data1,data2
    
    def sort(self,data):
        if len(data)==1:
            return data
        else:
            data1,data2=self.split(data)
            data1=self.sort(data1)
            data2=self.sort(data2)
            data=self.merge(data1,data2)
            
            return data
        
    
    def merge(self,data1,data2):
        i=j=0
        data=[]
        while i<len(data1) and j<len(data2):
            if data1[i]<data2[j]:
                data.append(data1[i])
                i+=1
            else:
                data.append(data2[j])
                j+=1
                
        if i==len(data1):
            data=data+data2[j:]
        else:
            data=data+data1[i:]
                
        return data
        

if __name__=='__main__':
    start=time.time()
#    import urllib.request
#    target_url='https://d3c33hcgiwev3.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1569542400&Signature=EiGJq74pfOp2QgTndOu~XOuUewF5iHWFuV~KajWAEnSKCy9uE6wcaOnIi8Q4rLZXxHyxJAKHqL3qG-Ioo~sT9FSBdHc773FRgwgjvK-vlvi395SoQwX~8Vs5bBt~55GgD1up~-ChnEiFDqQJXdPM7xHhaVnc4UvWC1MWrnZHbh4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
#    file = urllib.request.urlopen(target_url)
#    data=[]
#    for line in file:
#        a=line.decode("utf-8")
#        data.append(int(a.strip()))
#        
#    result=count_inversion(data)
#    print(result.number_inversion)     
    
    test=[6,7,15,1,2,3,4,5]
    result=merge_sort(test)
    print(result.result)
    end=time.time()
    print('time cost = ', end-start,'  sec ')