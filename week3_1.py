#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:28:41 2019

@author: yazi
"""
from random import shuffle
class quick_sort():
    def __init__(self,in_data):
        self.result,self.number=self.quicksort(in_data)
        
    def quicksort(self,data):
        length=len(data)
        if length<=1:
            return data,0
        else:
                
            shuffle(data)
            pivot=data[0]
            j=0
            for i in range(1,length):
                if pivot>data[i]:
                    j+=1
                    data=self.exchange(data,i,j)
                    
            
            data=self.exchange(data,0,j)        
            data[:j],num2=self.quicksort(data[:j])
            data[j+1:],num3=self.quicksort(data[j+1:])
            num1=self.countcompa(data)
            num=num1+num2+num3
            return data,num
    
    def countcompa(self,data):
        if len(data)<=1:
            return 0
        else:
            return(len(data)-1)
            
    def exchange(self,data,i,j):
        m=data[i]
        data[i]=data[j]
        data[j]=m
        return data

if __name__=='__main__':
   
    import urllib.request
    target_url='https://d3c33hcgiwev3.cloudfront.net/_32387ba40b36359a38625cbb397eee65_QuickSort.txt?Expires=1570492800&Signature=VX8-F3oArfcfq67lsaT33Sb3WnZXHTAXtB0NbPh5sdtpXZgg4s1fTsHUw46m7OXE5JquCKpbcnkbB2YzsW46o2iVccQ4r9d8JoHX8MAMmsRWCKtfMz9q6ZtCMZNPnIhg1Zmt4Q8EKEakTwfMC3GjijUi84RI1ubDLppBXGRTIPY_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
    file = urllib.request.urlopen(target_url)
    data=[]
    for line in file:
        a=line.decode("utf-8")
        data.append(int(a.strip()))        

    result=quick_sort(data)
    print(result.result)
    print(result.number)