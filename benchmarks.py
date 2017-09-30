# -*- coding: utf-8 -*-
"""
Edited on Tue May 11 18:46:20 2017

This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/himanshuRepo/GSA_PythonCode and matlab version of GSA at mathworks.

Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3), 2016 Ninth International Conference on,
            pp. 1-6,  IEEE."

Purpose: Defining the benchmark function code 
          and its parameters: function Name, lowerbound, upperbound, dimensions.
          The file is edited version of the code provided by Hossam Faris.

Code compatible:
 -- Python: 2.* or 3.*
"""

import numpy
import math


    
def F1(x):
  """ Spere Function """
  s=numpy.sum(x**2);
  return s



def getFunctionDetails(a):
  # [name, lb, ub, dim]
  param = {  0: ["F1",-100,100,30],
            }
  return param.get(a, "nothing")



