#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 15:51:15 2020

@author: yazi
"""

#A[n-1,v]=A[n,v]
#A[n,v]=min(A[n-1,v],min(A[n-1,w]+c(w,v)))
import urllib.request
from collections import defaultdict
import numpy as np
import copy

def load_graph(target_url):
    #graph : A->B load graph 
    file = urllib.request.urlopen(target_url)
    graph=defaultdict(dict)
    n_vertice=0
    n_edge=0
    n=0
    
    for line in file:
        n+=1
        a=line.decode("utf-8").strip()
        if n==1:
            n_vertice,n_edge = map(int,a.split())
        else:
            A,B,L=map(int,a.split())
            graph[A][B]=L
    
   
    return n_vertice,n_edge,graph

def addsource(graph,n_vertice):
    graph[n_vertice+1]={}
    for point in range(1,n_vertice+1):
        graph[n_vertice+1][point]=0
    return graph,n_vertice+1

def changeedge(graph,A):
    p={}
    for i,j in enumerate(A):
        p[i+1]=j
    
    for key1,value in graph.items():
        for key2,value2 in value.items():
            graph[key1][key2]=graph[key1][key2]+p[key1]-p[key2]
    
    return graph,p
        
    
def Johnsons_algorithm(graph,n_vertice):
    graph,n_vertice=addsource(graph,n_vertice)
    source=n_vertice
    A,B,detect=algorithm_Bellman_Ford(n_vertice,n_edge,graph,source)
    if A != detect:
        print("negative cycle detected")
        
    else:
         print("no negative cycle ")
         A.pop(-1)
         graph.pop(source)
         graph,p=changeedge(graph,A)
         return graph,p

def algorithm_Bellman_Ford(n_vertice,n_edge,graph,source):
    #A is the length for reach each destiation of the vertice from source choiced after n_vertice iteration
    #detect is A after n_vertice-1 iteration
    #B return the predecessor point
    #C conserve A
    A=[]
    B=[]
    C=[]
    detect=[]
    reach=[]
    reach2=[]
    reach.append(source)
    #initialize
    for j in range(1,n_vertice+1):
        if j==source:
            A.append(0)
            B.append(j)
        else:
            A.append(float('inf'))
            B.append(None)
            
    C=copy.deepcopy(A)    
    
    for n in range(n_vertice):
        print("iteration =",n)
        for w in reach:
            if w in graph:
                for v,l in graph[w].items():
                    reach2.append(v)
                    index=np.argmin([A[v-1],C[v-1],A[w-1]+l])
                    C[v-1]=min([A[v-1],C[v-1],A[w-1]+l])
                    if index==2:
                        B[v-1]=w
        reach=copy.deepcopy(list(set(reach2)))
        print(len(reach))
        reach2=[]
        A=copy.deepcopy(C)
        if n==n_vertice-2:
            detect=copy.deepcopy(A)
            
    
    return A,B,detect
    

def launch_dijikstra(source,n_vertice,graph):
    u=[]
    v=[i for i in range(1,n_vertice+1)]
    A={}
    key_v= dict.fromkeys(range(1,n_vertice+1),float('inf'))
    key_v[source]=0
    dijikstra(u,v,A,key_v,graph)
    return A

def dijikstra(u,v,A,key_v,graph):
    # u reached
    # v not reached
    # A dict for register restult of distance
    # key_v conserve distance of point not reached yet
 
    while v!=[]:
        key,value=min(key_v.items(), key=lambda x: x[1]) 
        A[key]=value
        u.append(key)
        v.remove(key)
        key_v.pop(key)
        
        if key in graph:
            for point,edge in graph[key].items():
                if point in v:
                    delete=key_v.pop(point)
                    minimum=min(delete,A.get(key,0)+edge)
                    key_v[point]=minimum
                

        dijikstra(u,v,A,key_v,graph)
        return u,v,A,key_v



if __name__=='__main__':
    target_url="https://d3c33hcgiwev3.cloudfront.net/_6ff856efca965e8774eb18584754fd65_g3.txt?Expires=1578700800&Signature=S1cLO2EAxmjdIlpRvBF~eg3Eq0zkHYaxg~aDekBgCSWpSUdfVG0Rs8F67acq92gXPkDe5W22gTh8ZjUVQ1v0UKysgs2YYgQlliWvCTRpbvGNCFCNKJOUKB7eoLkXiAtPyfWIAfWYRIeM44Zk8KydZnUllPGcI1~dy2v3k22mvto_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A"
    n_vertice,n_edge,graph=load_graph(target_url)
    # n_vertice=6
    # n_edge=7
    # graph={1:{2:-2},2:{3:-1},3:{1:4,4:2,6:-3},5:{4:1,6:-4}}
    graph,p=Johnsons_algorithm(graph,n_vertice)
    print("dejakstra")
    # graph={1:{2:2,3:4},2:{3:1,4:2},4:{5:2},3:{5:4}}
    # A,B,detect=algorithm_Bellman_Ford(n_vertice,n_edge,graph,1)
    # if A == detect:
    #     print("no negative cycle ")
    # else:
    #     print("negative cycle detected")
    minpair=[]
    for source in range(1,n_vertice):
        print("source = ",source)
        A=launch_dijikstra(source,n_vertice,graph)
        A.pop(source)
        for key,value in A.items():
            A[key]=value-p[source]+p[key]
        minpair.append(min(A.items(), key=lambda x: x[1])[1])
        
    print(min(minpair))