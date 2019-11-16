#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:15:39 2019

@author: yazi
"""

import numpy as np
import random
class min_cut():
    def __init__(self,matrix):
        self.result=self.contraction_alg(matrix)
        
    def contraction_alg(self,matrix):
        if matrix.shape==(2,2):
            return np.amax(matrix)
        else:
            i,j= random.sample(range(matrix.shape[0]),2)
            x=np.sum([matrix[i,:],matrix[j,:]],axis=0)
            matrix[i,:]=x
            matrix[:,i]=x
            matrix[i,i]=0
            matrix=np.delete(matrix,j,0)
            matrix=np.delete(matrix,j,1)
            return self.contraction_alg(matrix)
            
        
if __name__=='__main__':
#    a=np.zeros([4,4])
#    a=np.array([[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]])

     import urllib.request
     target_url='https://d3c33hcgiwev3.cloudfront.net/_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt?Expires=1571270400&Signature=ez6yGNsK~VRYjiucEmzRq~UGtnPlPa7AtIoFxjLILGZps37hzDDIsXEjahzxsr1dXmNEsTANeWlbZUYtz83iCBD9qPVMJpGZj2kwZ7uyU9uPxxcjQnMcdjYsD~Mc0dmmp59YheR2JGvvcT-edF9URwYPqqn6qM2Bt0g2Slyxiy0_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A' 
     file = urllib.request.urlopen(target_url)
     data=np.zeros([200,200])
     i=1
     for line in file:
         a=line.decode("utf-8").strip()
         a=a.split('\t')
         
         i+=1
         for number in a[1:]:

             data[int(a[0])-1,int(number)-1]=1
    
     result=[]
     for i in range(10000):
         
         t=min_cut(data)
         print(i,'times try : ',t.result)
         result.append(t.result)
    
     print(min(result))