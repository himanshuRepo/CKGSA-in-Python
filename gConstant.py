# -*- coding: utf-8 -*-
"""
Created on Mon May  11 21:20:52 2017

This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/7ossam81/EvoloPy

Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3),  

Purpose: Defining the gConstant function for calculating the Gravitational Constant

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy

def gConstant(l,iters):
    alfa = 20
    G0 = 100
    Gimd = numpy.exp(-alfa*float(l)/iters)
    G = G0*Gimd
    return G
