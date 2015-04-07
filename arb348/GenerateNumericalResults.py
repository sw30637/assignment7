'''
Module to create the numerical results. 

Created on Apr 5, 2015
@author: Adam Biesenbach
'''
import numpy as np

def CreateNumericalResults(cumu_ret, daily_ret):
    """ Compute the mean and STD of daily returns for each of the 
    positions, and save the results to a text file. """
    
    # axis = 0 says to collapse along the columns. 
    MeanDailyReturns = np.mean(daily_ret, axis=0)
    StandardDeviationReturns = np.std(daily_ret, axis=0)
    
    # Write the results to a text file. 
    with open('results.txt', 'w') as f:
        f.write('Here are the mean daily returns for the positions [1, 10, 100, 1000]: \n')
        f.write(str(MeanDailyReturns) + "\n")
        f.write(" ")
        f.write('Here are the standard deviations of daily returns for the positions [1, 10, 100, 1000]: \n')
        f.write(str(StandardDeviationReturns) + "\n")
    
    return (MeanDailyReturns, StandardDeviationReturns)