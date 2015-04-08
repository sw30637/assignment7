'''
Created by: Joseph Song (JLS731)
Assignment #7

Description: This function takes the list of positions and position_values and runs the simulations. 
Note that you can change the probability of the times you double your value and the number of trials.
'''

import numpy as np


def runSimulation(shares, share_value, num_trials = 10000, win_odd = 51):
    '''This function runs the investment simulations'''
    numpositions = len(shares)
    daily_ret = np.zeros((numpositions, num_trials))
    for i in range(0,numpositions):
        shareVal = share_value[i]
        for j in range(num_trials):
            cumu_ret = 0
            for k in range(shares[i]):
                randomNumber = np.random.random_integers(1,100,1)
                if randomNumber <= win_odd:
                    cumu_ret = cumu_ret + shareVal*2
                elif randomNumber > win_odd:
                    cumu_ret = cumu_ret
            daily_ret[i,j] = (cumu_ret/1000.) -1
                     
    return daily_ret

