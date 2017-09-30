# -*- coding: utf-8 -*-
"""
Edited on Thursday May 11 15:50:25 2017

This is the code for Chaotic Kbest Gravitational Search Algorithm (CKGSA)
Coded by: Himanshu Mittal, himanshu.mittal224@gmail.com
The code template used is similar to code given at link: https://github.com/7ossam81/EvoloPy and matlab version of GSA at mathworks.


Reference: "H. Mittal,R. Pal,A. Kulhari,and M. Saraswat, 
            “Chaotic Kbest gravitational search algorithm (CKGSA)”,
            In Contemporary Computing (IC3), 2016 Ninth International Conference on,
            pp. 1-6,  IEEE."

-- Main File: Calling the Chaotic Kbest Gravitational Search Algorithm(GSA) Algorithm 
                for minimizing of an objective Function
                The file is edited version of the code provided by Hossam Faris.

Code compatible:
 -- Python: 2.* or 3.*
"""

import CKGSA as ckgsa
import benchmarks
import csv
import numpy
import time


def selector(algo,func_details,popSize,Iter):
    function_name=func_details[0]
    lb=func_details[1]
    ub=func_details[2]
    dim=func_details[3]
    

    if(algo==0):
        x=ckgsa.CKGSA(getattr(benchmarks, function_name),lb,ub,dim,popSize,Iter)    
    return x
    
    
# Select optimizers
CKGSA= True # Code by Himanshu Mittal



# Select benchmark function
F1=True



Algorithm=[CKGSA]
objectivefunc=[F1] 
        
# Select number of repetitions for each experiment. 
# To obtain meaningful statistical results, usually 30 independent runs 
# are executed for each algorithm.
Runs=2

# Select general parameters for all optimizers (population size, number of iterations)
PopSize = 2
iterations= 2

#Export results ?
Export=True


#ExportToFile="YourResultsAreHere.csv"
#Automaticly generated name by date and time
ExportToFile="experiment"+time.strftime("%Y-%m-%d-%H-%M-%S")+".csv" 

# Check if it works at least once
atLeastOneIteration=False


# CSV Header for for the cinvergence 
CnvgHeader=[]

for l in range(0,iterations):
	CnvgHeader.append("Iter"+str(l+1))


for i in range (0, len(Algorithm)):
    for j in range (0, len(objectivefunc)):
        if((Algorithm[i]==True) and (objectivefunc[j]==True)): # start experiment if an Algorithm and an objective function is selected
            for k in range (0,Runs):
                
                func_details=benchmarks.getFunctionDetails(j)
                x=selector(i,func_details,PopSize,iterations)
                if(Export==True):
                    with open(ExportToFile, 'a') as out:
                        writer = csv.writer(out,delimiter=',')
                        if (atLeastOneIteration==False): # just one time to write the header of the CSV file
                            header= numpy.concatenate([["Optimizer","objfname","startTime","EndTime","ExecutionTime"],CnvgHeader])
                            writer.writerow(header)
                        a=numpy.concatenate([[x.Algorithm,x.objectivefunc,x.startTime,x.endTime,x.executionTime],x.convergence])
                        writer.writerow(a)
                    out.close()
                atLeastOneIteration=True # at least one experiment
                
if (atLeastOneIteration==False): # Faild to run at least one experiment
    print("No Optomizer or Cost function is selected. Check lists of available optimizers and cost functions") 
        
        
