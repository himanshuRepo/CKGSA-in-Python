# -*- coding: utf-8 -*-
"""
Edited on Tue May 11 17:06:19 2017

This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
@author: Himanshu Mittal, himanshu.mittal224@gmail.com

Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3),  

Purpose: Defining the solution class
                The file is edited version of the code provided by Hossam Faris.
 
Code compatible:
 -- Python: 2.* or 3.*

"""

class solution:
    def __init__(self):
        self.best = 0
        self.bestIndividual=[]
        self.convergence = []
        self.optimizer=""
        self.objfname=""
        self.startTime=0
        self.endTime=0
        self.executionTime=0
        self.lb=0
        self.ub=0
        self.dim=0
        self.popnum=0
        self.maxiers=0
