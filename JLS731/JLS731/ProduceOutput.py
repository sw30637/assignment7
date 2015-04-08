'''
Created by: Joseph Song (JLS731)
Assignment #7

Description: This function creates the histograms and table output
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from RunSimulations import *

def computeStats(simulationResults, positions):
    '''Creates the table with the different positions, expected values and st. deviation'''
    ev = np.mean(simulationResults, axis = 1)
    stdev = np.std(simulationResults, axis = 1)
    data = np.vstack((positions, ev, stdev))
    data = np.transpose(data)
    order = ['Positions','Expected Value', 'Standard Deviation']
    dataTable = {'Positions': data[:,0], 'Expected Value':data[:,1], 'Standard Deviation': data[:,2]}
    frame = pd.DataFrame(dataTable, columns=order)
    frame.to_csv('results.txt')


def produceHistogram(simulationResults, positions):
    '''Creates the histogram with the simulations results'''
    row, col = simulationResults.shape
    for i in range(row):
        plt.hist(simulationResults[i,:], 100, range=[-1,1])
        plt.xlim(-1,1)
        plt.savefig('histogram_%04d_pos.pdf' % (positions[i]))
        plt.close()
