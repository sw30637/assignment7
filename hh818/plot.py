'''
Created on Apr 8, 2015

@author: ds-ga-1007
'''
import matplotlib.pyplot as plt
import numpy as np

def plotResults(daily_ret, num_trial, fileName):
    '''take daily_ret and plot histogram'''
    trialSum = []
    for i in range(num_trial):
        trialSum.append(np.sum(daily_ret[i]))
    plt.hist(trialSum, 100, range = [-1,1])
    plt.savefig(fileName)
    plt.close()
    
    print str(fileName) + ' saved'