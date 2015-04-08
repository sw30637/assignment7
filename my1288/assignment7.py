import numpy as np
import matplotlib.pylab as plt
from CalculateReturn import *
from UserInput import *



if __name__ == '__main__':

	# Get the user input
	GetUserInput()
	CheckUserInput()

	# Initialize the Investment Instrument
	print "Running 10000 trials...\n"

	# Define the class
	ret_ins = InvestmentTrials([1,10,100,1000],10000,1000)
	ret_ins.CalculateTrials()
