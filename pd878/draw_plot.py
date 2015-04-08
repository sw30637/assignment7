'''
Created on Apr 5, 2015

@author: Pan Ding pd878package@nyu.edu
'''
import matplotlib.pyplot as plt

def plot_simulation(input_list, filename):
    '''takes a list of daily_ret, and '''
    plt.hist(input_list, 100, range = [-1,1])
    plt.savefig(filename)
    plt.close()
    print 'Figure is saved as %s.' %filename