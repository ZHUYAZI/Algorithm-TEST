#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 12:11:20 2019

@author: yazi
"""

import time
    
class merge_sort():
    def __init__(self,in_data):
        self.result,self.inv_num=self.sort_count(in_data)
        
        
    def split(self,data):
        data1=data[0:len(data)//2]
        data2=data[len(data)//2:len(data)]
        return data1,data2
    
    def sort_count(self,data):
        if len(data)==1:
            return data,0
        else:
            data1,data2=self.split(data)
            data1,num1=self.sort_count(data1)
            data2,num2=self.sort_count(data2)
            num3=self.countsplit(data1,data2)
            data=self.merge(data1,data2)
            
            num=num1+num2+num3
            return data,num
        
    def countsplit(self,data1,data2):
        count=0
        i=j=0
        while i<len(data1) and j<len(data2):
            if data1[i]>data2[j]:
                count+=(len(data1)-i)
                j+=1
            else:
                i+=1
        return count
        
        
        
        
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
    import urllib.request
    target_url='https://d3c33hcgiwev3.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1569542400&Signature=EiGJq74pfOp2QgTndOu~XOuUewF5iHWFuV~KajWAEnSKCy9uE6wcaOnIi8Q4rLZXxHyxJAKHqL3qG-Ioo~sT9FSBdHc773FRgwgjvK-vlvi395SoQwX~8Vs5bBt~55GgD1up~-ChnEiFDqQJXdPM7xHhaVnc4UvWC1MWrnZHbh4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
    file = urllib.request.urlopen(target_url)
    data=[]
    for line in file:
        a=line.decode("utf-8")
        data.append(int(a.strip()))
        
    result=merge_sort(data)
#    print(result.number_inversion)     
    
#    test=[3,2,1]
#    result=merge_sort(test)
    print(result.result)
    print(result.inv_num)
    end=time.time()
    print('time cost = ', end-start,'  sec ')