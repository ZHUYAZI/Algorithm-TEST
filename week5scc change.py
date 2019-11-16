#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 08:51:02 2019

@author: yazi
"""

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def calculate(G,boolen_graph,list_order,leader_list):
    que=sorted(list_order.keys(), key=lambda x: list_order[x],reverse=True)
    t=0
    for key in que:
        if boolen_graph[key]==0:
            leader=key
            boolen_graph,leader,leader_list,t,list_order=DFS(G,key,boolen_graph,leader,leader_list,t,list_order)
    return list_order,leader_list
            
    
def DFS(G,node,boolen_graph,leader,leader_list,t,list_order):
    boolen_graph[node]=1
    leader_list[node]=leader
    for point in G[node]:
        if boolen_graph[point]==0:
            boolen_graph,leader,leader_list,t,list_order=DFS(G,point,boolen_graph,leader,leader_list,t,list_order)
    t+=1
    list_order[node]=t
    return boolen_graph,leader,leader_list,t,list_order
    

    
def main():
    from collections import defaultdict
    import copy
    path='/home/yazi/Downloads/SCC.txt'
    file = open(path,'r') 
    data = file.readlines()
    graph=defaultdict(list)
    graph_inv=defaultdict(list)
    for line in data:
        line=line.strip()
        key,value=line.split(' ')
        print(int(key)/875714)
        graph[int(key)].append(int(value))
        graph_inv[int(value)].append(int(key))
    
    print('finished')
    boolen1=dict.fromkeys(list(range(1,875715)), 0)    
    boolen2=copy.deepcopy(boolen1)
    order_list={key:value for (key,value) in zip(range(1,875715),range(1,875715))}
    leader_list=dict.fromkeys(list(range(1,875715)), 0)

    order_list,_=calculate(graph_inv,boolen1,order_list,leader_list)
    _,result=calculate(graph,boolen2,order_list,leader_list)
    
    print(result)
    count_dict={}
    for key,value in result.items():
        count_dict[value]=count_dict.get(value,0)+1
    print(count_dict)
    print(sorted(count_dict.values(),reverse=True)[0:5])
        
        
thread = threading.Thread(target=main)
thread.start()
