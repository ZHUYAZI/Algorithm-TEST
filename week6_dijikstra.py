#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:30:04 2019

@author: yazi
"""

def launch(data):
    length=200
    u=[]
    v=[i for i in range(1,length+1)]
    A={}
    key_v= dict.fromkeys(range(2,length+1),1000000)
    key_v[1]=0
    dijikstra(u,v,A,key_v,data)
    return A
    
    
def dijikstra(u,v,A,key_v,data):
    while v!=[]:
        key,value=min(key_v.items(), key=lambda x: x[1]) 
        A[key]=value
        u.append(key)
        v.remove(key)
        key_v.pop(key)
        
        
        

        for edge in data[key]:
            if edge[0] in v:
                delet=key_v.pop(edge[0])
                minimum=min(delet,A.get(key,0)+edge[1])
                key_v[edge[0]]=minimum
                

        dijikstra(u,v,A,key_v,data)
        return u,v,A,key_v

        
if __name__=='__main__':
#    graph={1:[(2,1),(4,4)],2:[(3,2)],3:[(4,3)],4:[(2,5)]}

    path='/home/yazi/Downloads/shortestpath.txt'
    file = open(path,'r') 
    data = file.readlines()
    i=0
    graph={}
    for line in data:
        
        text=line.strip().split('\t')

        graph[int(text[0])]=[]
        
        for element in text[1:]:

            key,value=element.split(",")
            graph[int(text[0])].append((int(key),int(value)))
        
    
    A=launch(graph)
    print(A)
