'''
Created on Apr 5, 2015

@author: Pan Ding pd878package@nyu.edu
'''


import sys
import random
import matplotlib.pyplot as plt
import numpy as np

import user_input as ui
import simulation as si
import draw_plot as dp



if __name__ == "__main__":
    positions = ui.take_positions()
    num_trials = ui.take_num_trials()
    task = si.simulation(positions, num_trials) # creates a class of simulation

    result_file = open('results.txt', 'w') # create an empty txt file to write

    for position in positions:
        position_value = task.total_investment/position
        daily_ret = task.simulate_daily_return(position_value, num_trials)
        # saves the simulations of daily return in a list

        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        result_file.write('For position %d, mean is %f, standard deviation is %f.\n' %(position, mean, std))
        # writes the numerical result into the txt file
        print '\nFor position %d, mean is %f, standard deviation is %f. \nResult is saved to results.txt' %(position, mean, std)
        
        # plot the simulation and save the plot.
        plot_name = 'histogram_%s_pos.pdf' %position
        dp.plot_simulation(daily_ret, plot_name)
        
    result_file.close()
    
    print '\nEnd of program.'
