'''
Created on Apr 5, 2015

@author: Pan Ding pd878package@nyu.edu
'''
import random


class simulation:
    '''creates a class of simulation. 
    it takes a list of positions and an integer to define 
    the number of trials for the simulation.'''
    
    def __init__(self, positions, num_trials):
        self.positions = positions
        self.num_trials = num_trials
        self.prob = 0.51 # the probability that the return is 1
        self.total_investment = 1000 

    def simulate_return(self):
        '''simulates the return of one trial'''
        if random.random() < self.prob:
            return 1.0 
        else:
            return -1.0

    def simulate_cumu_return(self, position_value, num_trials):
        '''takes position_value and num-trials, 
        simulates the investment for num_trials times, 
        saves the cumulative return of each trial in a list'''
        cumu_return = []
        for trial in range(num_trials): #runs simulation for num_trails times
            each_return = 0
            num_positions = int(self.total_investment/position_value)
            for i in range(num_positions):  # runs simulation for each portion
                each_return = each_return + position_value*(self.simulate_return()+1)
            cumu_return.append(each_return)
        return cumu_return

    def simulate_daily_return(self, position_value, num_trials):
        '''takes position_value and num_trails, 
        simulates the investment for num_trials times, 
        saves the daily return of each trial in a list'''
        daily_return = []
        cumu_return = self.simulate_cumu_return(position_value, num_trials)
        for i in range(num_trials):
            daily_return.append(cumu_return[i]/self.total_investment - 1)
        return daily_return

