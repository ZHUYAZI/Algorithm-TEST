#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 17:03:22 2019

@author: yazi
"""
def heapfy_small(data:list,i:int):
    length=len(data)
    l=2*i+1
    r=2*i+2
    smallest=i
    if l<length and data[l]<data[i] :
        smallest=l
    if r<length and data[r]<data[smallest]:
        smallest=r
    if smallest!=i:
        data[i],data[smallest]=data[smallest],data[i]
        
        heapfy_small(data,smallest)
    return data
    
def heapfy_big(data:list,i:int):
    length=len(data)
    l=2*i+1
    r=2*i+2
    biggest=i
    if l<length and data[l]>data[i] :
        biggest=l
    if r<length and data[r]>data[biggest]:
        biggest=r
    if biggest!=i:
        data[i],data[biggest]=data[biggest],data[i]
        
        heapfy_big(data,biggest)
    
    return data

def heapfy(data:list,indication:str):
    length=len(data)
    if indication=='big':
        for i in range(length//2,-1,-1):
            heapfy_big(data,i)
           
    else:
        for i in range(length//2,-1,-1):
            heapfy_small(data,i)
            
    return data


if __name__=='__main__':

#    46831213

    data=[]
    import urllib.request
    target_url='https://d3c33hcgiwev3.cloudfront.net/_6ec67df2804ff4b58ab21c12edcb21f8_Median.txt?Expires=1572825600&Signature=G~0QPn8qvUgy4b~lVV8NyoIwwZ0uaMq0mmCboM6IAwlOIaJkJHf0O3rKUKLvHesfrzp-A54eoxMFyL6zQbWXlGLRaI9wWzsgqB7YX8LAzk9EAU~HeoqRFgGjBzmpj5dJUIY4mfO27LXPt1Rn1spK2iAL0NMW~n57ZyAfZ9UG2WI_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
    file = urllib.request.urlopen(target_url)
    for line in file:
        a=line.decode("utf-8").strip()
        data.append(int(a))
#        
        
    
    length=len(data)
    Low=[]
    High=[]
    Sum=0
    Sum+=data[0]
    print(data[0])
    print(data[0])
    if data[0]<data[1]:
        Low.append(data[0])
        High.append(data[1])
    else:
        Low.append(data[1])
        High.append(data[0])
    Sum+=Low[0]   
    heapfy(Low,'big')
    heapfy(High,'Small')
 

    for i in range(2,length):
        if data[i]>High[0]:
            High.append(data[i])            
        elif data[i]<Low[0] :
            Low.append(data[i])
        else:
            Low.append(data[i])
            Low[0],Low[-1]=Low[-1],Low[0]
            
        if len(Low)==len(High):
            print(Low[0])
            Sum+=Low[0]    
        elif len(Low)==len(High)+1:
            print(Low[0])
            Sum+=Low[0]
        elif len(Low)==len(High)-1:
            print(High[0])
            Sum+=High[0]
        elif len(Low)==len(High)+2:
            ele=Low.pop(0)
            heapfy(Low,'big')
            High.append(ele)
            High[0],High[-1]=High[-1],High[0]
            heapfy(High,'small')
            
            print(Low[0])
            Sum+=Low[0]
        else:
            ele=High.pop(0)
            heapfy(High,'small')
            Low.append(ele)
            Low[0],Low[-1]=Low[-1],Low[0]
            heapfy(Low,'big')
            
            print(Low[0])
            Sum+=Low[0]
    
    print('media sum =',Sum)
        
