#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 15:15:32 2019

@author: yazi
"""

import math



def get_number(num):
    if num==0:
        return 1
    else:
        return int(math.log10(num))+1
    

def product(x1,x2):
    if get_number(x1)==1 or get_number(x2)==1:
        return x1*x2
    else:
        a,b=divde_in_two(x1)
        c,d=divde_in_two(x2)
        s1=product(a,c)
        s2=product(b,d)
        s3=product(a,d)
        s4=product(b,c)
        n1=get_number(b)
        n2=get_number(d)
        result=s1*10**(n1+n2)+s2+s3*10**n1+s4*10**n2
        return result

def divde_in_two(x):
    number=get_number(x)
    left=number//2
    right=number-left
    left_x=x//10**right
    right_x=x%10**right
    while get_number(left_x)+get_number(right_x) != number:
        left+=1
        right-=1
        left_x=x//10**right
        right_x=x%10**right
        
    return left_x,right_x


if __name__=='__main__':
    x1=3141592653589793238462643383279502884197169399375105820974944592
    x2=40
    
    real_reslut=x1*x2
    my_result=product(x1,x2)
    
    print('real_reslut = ',real_reslut)
    print(' my_result = ', my_result)
    print(real_reslut==my_result)
    