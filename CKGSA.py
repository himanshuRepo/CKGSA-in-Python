# -*- coding: utf-8 -*-
"""
This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/himanshuRepo/GSA_PythonCode and matlab version of GSA at mathworks.

Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3), 2016 Ninth International Conference on,
            pp. 1-6,  IEEE."

Purpose: Main file of Chaotic Kbest Gravitational Search Algorithm(CKGSA) 
            for minimizing of the Objective Function

Code compatible:
 -- Python: 2.* or 3.*
"""

import random
import numpy
import math
from solution import solution
import time
import massCalculation
import gConstant
import ckgfield
import move

        
def CKGSA(objf,lb,ub,dim,PopSize,iters):
    # CKGSA parameters
    ElitistCheck =1
    Rpower = 1 
     
    s=solution()
        
    """ Initializations """
    Variant = 1
    vel=numpy.zeros((PopSize,dim))
    fit = numpy.zeros(PopSize)
    M = numpy.zeros(PopSize)
    gBest=numpy.zeros(dim)
    gBestScore=float("inf")
    
    pos=numpy.random.uniform(0,1,(PopSize,dim)) *(ub-lb)+lb
    
    convergence_curve=numpy.zeros(iters)
    
    print("CKGSA is optimizing  \""+objf.__name__+"\"")    
    
    timerStart=time.time() 
    s.startTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    
    for l in range(0,iters):
        for i in range(0,PopSize):
            l1 = [None] * dim
            l1=numpy.clip(pos[i,:], lb, ub)
            pos[i,:]=l1

            #Calculate objective function for each particle
            fitness=[]
            fitness=objf(l1)
            fit[i]=fitness
    
                
            if(gBestScore>fitness):
                gBestScore=fitness
                gBest=l1
        
        """ Calculating Mass """
        M = massCalculation.massCalculation(fit,PopSize,M)

        """ Calculating Gravitational Constant """        
        G = gConstant.gConstant(l,iters)        
        
        """ Calculating Gfield """        
        acc = ckgfield.ckgfield(PopSize,dim,pos,M,l,iters,G,ElitistCheck,Rpower,Variant)
        
        """ Calculating Position """        
        pos, vel = move.move(PopSize,dim,pos,vel,acc)
        
        convergence_curve[l]=gBestScore
      
        if (l%1==0):
               print(['At iteration '+ str(l+1)+ ' the best fitness is '+ str(gBestScore)]);
    timerEnd=time.time()  
    s.endTime=time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime=timerEnd-timerStart
    s.convergence=convergence_curve
    s.Algorithm="CKGSA"
    s.objectivefunc=objf.__name__

    return s
         
    
