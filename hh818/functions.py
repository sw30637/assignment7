'''
Created on Apr 3, 2015

@author: ds-ga-1007
'''
import numpy as np

def investmentInstrument(positions, num_trial):
    '''simulate 'num_trials' number of results of buying 'positions' number of shares using $1000'''
    #how much is each share ($1, $10, $100, or $1000)
    position_value = 1000/positions
    daily_ret = np.arange(num_trial*positions, dtype = float).reshape(num_trial, positions)
    for trial in range(num_trial):
        for position in range(positions):
            daily_ret[trial, position] = (trialResult(position_value)/1000.)
    return daily_ret
        

def simulateResults():
    '''return a result, either 0 where you lose all money (49% chance) or 2 where you double your money (51% chance)'''
    possibleResults = [-1, 1]
    results = np.random.choice(possibleResults, p = [0.49, 0.51])
    return results

def trialResult(position_value):
    '''return result of each position in each trial'''
    cumu_ret = simulateResults() * position_value
    return cumu_ret

