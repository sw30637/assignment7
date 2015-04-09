'''
Created on Apr 7, 2015

@author: ds-ga-1007
'''
import numpy as np

def mean(daily_ret, num_trial):
    '''take the mean of daily_ret'''
    trialSum = []
    for i in range(num_trial):
        tempSum = np.sum(daily_ret[i])
        trialSum.append(tempSum)
    mean = np.mean(trialSum)
    
    return mean

def sd(daily_ret):
    '''take the standard deviation of daily_ret'''
    sd = np.std(daily_ret)
    
    return sd