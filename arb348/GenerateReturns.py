'''
This module holds the functions which take in the user input (the positions data and the number of trials)
and generates the cumu_ret and daily_ret arrays.

Created on Apr 2, 2015
@author: Adam Biesenbach
'''

import numpy as np
import random 

def GenerateDailyReturns(positions, num_trials):
    """This function takes as input the positions list fed by the user, and computes
    the cumu_ret and daily_ret series. """

    # Initialize empty arrays to the correct size.      
    cumu_ret = np.zeros(shape = (num_trials.TrialNumber, len(positions.PositionsInList))) 
    daily_ret = np.zeros(shape = (num_trials.TrialNumber, len(positions.PositionsInList)))
    
    position_value = [1000/x for x in positions.PositionsInList] 
    
    # For each position, and each trial, generative the cumulative returns for that position and trial, and put the 
    # results in the right position in the arrays. 
        
    for i, EachPosition in enumerate(positions.PositionsInList):   
        for trials in range(num_trials.TrialNumber):
            CurrentPositionValue = position_value[i]
            cumu_ret[trials, i] = CumulateReturns(CurrentPositionValue, EachPosition)
            daily_ret[trials, i] = (cumu_ret[trials, i]/1000)-1            
    return (cumu_ret, daily_ret)

def CumulateReturns(CurrentPositionValue, EachPosition): 
    """ This function takes in a position size and the number of times the 
    investment needs to be calculated. For 1 $1000 investment 
    this is one calculation, for 10 $100 it's ten, etc."""
    
    # Initialize an intermediate array that's empty, that will be as long as the
    # number of times that we need to repeat the experiment (in this case, 
    # the length will be the same as the corresponding value in the 'position_value' array,
    # which we index with the i index. 
    
    pre_cum_ret = np.zeros(shape=(EachPosition))
    for rep in range(EachPosition): 
        pre_cum_ret[rep] = CurrentPositionValue*(1+DetermineReturns(0.51))
    
    # Once we've determined all the outcomes, we sum across them to get 
    # the cumulative returns for that number of shares.
     
    SummedPreCumReturns = np.sum(pre_cum_ret)
    return SummedPreCumReturns
    
def DetermineReturns(p):
    """A function which determines the returns enjoyed by the investor, 
    with a return of 100% p percent of the time and -100% 1-p percent. """

    if random.random() < p:
        return 1
    else:
        return -1    