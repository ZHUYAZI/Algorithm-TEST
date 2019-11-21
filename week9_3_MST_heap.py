#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:49:09 2019

@author: yazi
"""

from collections import defaultdict
import sys
import random
class Heap():
    def __init__(self):
        self.array=[]
        self.size=0
        self.pos=[]
        
    def newMinHeapNode(self,v,dist):
        minHeapNode=[v,dist]
        return minHeapNode
    
    def swapMinHeapNode(self,a,b):
        self.array[a],self.array[b]=self.array[b],self.array[a]
        
    def minHeapify(self,idx):
        smallest=idx
        left=2*idx+1
        right=2*idx+2
        if left<self.size and self.array[left][1]<self.array[smallest][1]:
            smallest=left
        if right < self.size and self.array[right][1] < self.array[smallest][1]: 
            smallest = right 
        if smallest !=idx:
             # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
            self.minHeapify(smallest) 
            
    def extractMin(self):
        if self.isEmpty() == True: 
            return
        root = self.array[0] 
        lastNode = self.array[self.size - 1] 
        self.array[0],self.array[self.size - 1] = lastNode,root
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.minHeapify(0) 
        return root
    
    def isEmpty(self): 
        return True if self.size == 0 else False
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
        
        i = self.pos[v] 
        i=int(i)
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is not  
        # hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
            
def printArr(parent, n): 
    for i in range(1, n): 
        print ("% d - % d" % (parent[i], i) )

class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = defaultdict(list) 
    def addEdge(self, src, dest, weight): 
  
        # Add an edge from src to dest.  A new node is 
        # added to the adjacency list of src. The node  
        # is added at the begining. The first element of 
        # the node has the destination and the second  
        # elements has the weight 
        newNode = [dest, weight] 
        self.graph[src].insert(0, newNode) 
  
        # Since graph is undirected, add an edge from  
        # dest to src also 
        newNode = [src, weight] 
        self.graph[dest].insert(0, newNode) 
        
    # The main function that prints the Minimum  
    # Spanning Tree(MST) using the Prim's Algorithm.  
    # It is a O(ELogV) function 
    def PrimMST(self): 
        # Get the number of vertices in graph 
        V = self.V   
          
        # key values used to pick minimum weight edge in cut 
        key = []    
          
        # List to store contructed MST 
        parent = []  
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        # Initialize min heap with all vertices. Key values of all 
        # vertices (except the 0th vertex) is is initially infinite 
        for v in range(V): 
            parent.append(-1) 
            key.append(sys.maxsize) 
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
            minHeap.pos.append(v) 
  
        # Make key value of 0th vertex as 0 so  
        # that it is extracted first 
#        minHeap.pos[0] = 0
        choice=random.randint(0, 499)
        key[choice] = 0
        minHeap.decreaseKey(choice, key[choice]) 
  
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # not yet added in the MST. 
        Ledge=0
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0] 
            Ledge+=newHeapNode[1]
            # Traverse through all adjacent vertices of u  
            # (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less than 
                # its previously calculated distance 
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                    key[v] = pCrawl[1] 
                    parent[v] = u 
  
                    # update distance value in min heap also 
                    minHeap.decreaseKey(v, key[v]) 
  
#        printArr(parent, V) 
        print('Ledge = ',Ledge)
        

      
#graph = Graph(4) 
#graph.addEdge(0, 1, 1) 
#graph.addEdge(1, 3, 2) 
#graph.addEdge(2, 0, 4) 
#graph.addEdge(3, 2, 5) 
#graph.addEdge(3, 0, 3) 
##graph.addEdge(2, 8, 2) 
##graph.addEdge(2, 5, 4) 
##graph.addEdge(3, 4, 9) 
##graph.addEdge(3, 5, 14) 
##graph.addEdge(4, 5, 10) 
##graph.addEdge(5, 6, 2) 
##graph.addEdge(6, 7, 1) 
##graph.addEdge(6, 8, 6) 
##graph.addEdge(7, 8, 7) 
#graph.PrimMST()
import urllib.request
target_url='https://d3c33hcgiwev3.cloudfront.net/_d4f3531eac1d289525141e95a2fea52f_edges.txt?Expires=1573862400&Signature=MDIB9uIEtSnAD6OLcGdmZ0JOdcHOGnxHij8-prRhz0JMlf~XVtz-7aopZHR5-UkHsjt~yh4Khi~kv5zPf9vXfkTfY8g55fYupaOUu7dt4UeNaz8WOZXHOEq6qRUaRZjRlVNoRs4TjXGlFWWxLuWIRviQO7pNsXZTBlyCPya1MQo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
file = urllib.request.urlopen(target_url)
n=0
theArray=defaultdict(dict)
node=0
edge=0
for line in file:
    n+=1
    a=line.decode("utf-8").strip()
    if n==1:
        node,edge=a.split( )
        graph = Graph(int(node))
    else:
        n1,n2,l=a.split( )
        graph.addEdge(int(n1)-1, int(n2)-1, int(l))


print(n)
graph.PrimMST()
