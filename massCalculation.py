# -*- coding: utf-8 -*-
"""
Created on Mon May  1 21:20:52 2017

This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/himanshuRepo/GSA_PythonCode and matlab version of GSA at mathworks.


Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3),  

Purpose: Defining the massCalculation function for calculating the mass

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy 

def massCalculation(fit,PopSize,M):
    Fmax = max(fit)
    Fmin = min(fit)
    Fsum = sum(fit)        
    Fmean = Fsum/len(fit)
        
    if Fmax == Fmin:
        M = numpy.ones(PopSize)
    else:
        best = Fmin
        worst = Fmax
        
    for p in range(0,PopSize):
        M[p] = (fit[p]-worst)/(best-worst)
            
    Msum=sum(M)
    for q in range(0,PopSize):
        M[q] = M[q]/Msum
            
    return M
