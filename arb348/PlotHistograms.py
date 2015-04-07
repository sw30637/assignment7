'''
A module to create the histograms of our output.

Created on Apr 2, 2015
@author: Adam Biesenbach
'''

import matplotlib.pyplot as plt
import os, errno

def PlotHistograms(daily_ret):
    """Save the results of our analysis to pdf files 
    that display the results in histograms."""

    silentremove("histogram_0001_pos.pdf")
    plt.hist(daily_ret[:,0], bins=100, range=(-1,1))
    plt.xlim(-1, 1)
    plt.savefig("histogram_0001_pos.pdf")
    plt.clf()
  
    silentremove("histogram_0010_pos.pdf")    
    plt.hist(daily_ret[:,1], bins=100, range=(-1,1))
    plt.xlim(-1, 1)   
    plt.savefig("histogram_0010_pos.pdf")    
    plt.clf()
    
    silentremove("histogram_0100_pos.pdf")                
    plt.hist(daily_ret[:,2], bins=100, range=(-1,1))
    plt.xlim(-1, 1)
    plt.savefig("histogram_0100_pos.pdf")  
    plt.clf()

    silentremove("histogram_1000_pos.pdf")                
    plt.hist(daily_ret[:,3], bins=100, range=(-1,1))
    plt.xlim(-1, 1)
    plt.savefig("histogram_1000_pos.pdf")  
    plt.clf() 

def silentremove(filename):
    """ A function that removes a file if it exists."""
    try:
        os.remove(filename)
    except OSError as e: 
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured