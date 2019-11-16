#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 20:16:37 2019

@author: yazi
"""

import sys, threading
sys.setrecursionlimit(800000)
threading.stack_size(67108864)

class scc():
    def __init__(self,graph_inv:dict,graph:dict,boolen1:dict,order_list:dict,leader_list:dict,boolen2:dict)->None:
        self.t=0
        self.boolen_graph=boolen1
        self.list_order=order_list
        self.leader=0
        self.leader_list=leader_list
        self.calculate(graph_inv)
        self.boolen_graph=boolen2
        self.calculate(graph)
        
    def calculate(self,G):
        que=sorted(self.list_order.keys(), key=lambda x: self.list_order[x],reverse=True)
        for key in que:
            if self.boolen_graph[key]==0:
                self.leader=key
                self.DFS(G,key)
                
    
    def DFS(self,G,node):
        self.boolen_graph[node]=1
        self.leader_list[node]=self.leader
        for point in G[node]:
            if self.boolen_graph[point]==0:
                self.DFS(G,point)
        self.t+=1
        self.list_order[node]=self.t
        
        
   
            

def main():
    import copy
    from collections import defaultdict
#    graph_inv={1:[7],7:[4,9],4:[1],9:[6],6:[3,8],3:[9],8:[2],2:[5],5:[8]}
#    graph={1:[4],4:[7],7:[1],9:[7,3],3:[6],6:[9],8:[6,5],5:[2],2:[8]}
#    boolen1=dict.fromkeys(list(range(1,10)), 0)
#    boolen2=copy.deepcopy(boolen1)
#    order_list={key:value for (key,value) in zip(range(1,10),range(1,10))}
#    leader_list=dict.fromkeys(list(range(1,10)), 0)
#    result=scc(graph_inv,graph,boolen1,order_list,leader_list,boolen2)
#    l=result.leader_list
#    count_dict={}
#    for key,value in l.items():
#        count_dict[value]=count_dict.get(value,0)+1
 
    import urllib.request
    target_url='https://d3c33hcgiwev3.cloudfront.net/_410e934e6553ac56409b2cb7096a44aa_SCC.txt?Expires=1571788800&Signature=IqG949lL3afgL6~7150t0yzjCTll8~xIgiQ5xfDoEvCD6ctv7TBt~JAZuOkBb71~39S-AtUmGjobyOgZnCNQ-ob7lurldOdZcPhxEIko-CV08ivyGR7idj2V3Ky709IsnhoOjD9NXeBLvE8C9LCI93n1o3qVcGDy6TKelZHzfIU_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
    file = urllib.request.urlopen(target_url)
    graph=defaultdict(list)
    graph_inv=defaultdict(list)
    for line in file:
        a=line.decode("utf-8").strip()
        key,value=a.split(' ')
        print(int(key)/875714)
        graph[int(key)].append(int(value))
        graph_inv[int(value)].append(int(key))
        
    boolen1=dict.fromkeys(list(range(1,875715)), 0)    
    boolen2=copy.deepcopy(boolen1)
    order_list={key:value for (key,value) in zip(range(1,875715),range(1,875715))}
    leader_list=dict.fromkeys(list(range(1,875715)), 0)
    result=scc(graph_inv,graph,boolen1,order_list,leader_list,boolen2)
    
    l=result.leader_list
    count_dict={}
    for key,value in l.items():
        count_dict[value]=count_dict.get(value,0)+1
    
    print(sorted(count_dict.values(),reverse=True)[0:5])
    return count_dict
    

thread = threading.Thread(target=main)
thread.start()
