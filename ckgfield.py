# -*- coding: utf-8 -*-
"""
This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/himanshuRepo/GSA_PythonCode and matlab version of GSA at mathworks.

Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3),  

Purpose: Defining the cKgfield function for calculating the Force and acceleration

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import random
import math

def ckgfield(PopSize,dim,pos,M,l,iters,G,ElitistCheck,Rpower,Variant):
    final_per = 2
    if ElitistCheck == 1:
        ##### Kbest as per CKGSA (eq. 15)
        if Variant ==1:
            z=random.random()
            z=4*z*(1-z)
            kbest= (PopSize - 2)*((iters - l)/iters)+2*z
        
        else: #### Kbest as per original GSA (eq. 3)
            kbest=final_per+(1-l/iters)*(100-final_per) 
        
        kbest = round(PopSize*kbest/100)
    else:
        kbest = PopSize
            
    kbest = int(kbest)
    ds = sorted(range(len(M)), key=lambda k: M[k],reverse=True)
        
    Force = numpy.zeros((PopSize,dim))
    # Force = Force.astype(int)
    
    for r in range(0,PopSize):
        for ii in range(0,kbest):
            z = ds[ii]
            R = 0
            if z != r:                    
                x=pos[r,:]
                y=pos[z,:]
                esum=0
                imval = 0
                for t in range(0,dim):
                    imval = ((x[t] - y[t])** 2)
                    esum = esum + imval
                    
                R = math.sqrt(esum)
                
                for k in range(0,dim):
                    randnum=random.random()
                    Force[r,k] = Force[r,k]+randnum*(M[z])*((pos[z,k]-pos[r,k])/(R**Rpower+numpy.finfo(float).eps))
                    
    acc = numpy.zeros((PopSize,dim))
    for x in range(0,PopSize):
        for y in range (0,dim):
            acc[x,y]=Force[x,y]*G
    return acc
