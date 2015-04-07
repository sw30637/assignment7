# Name: 	investment.py
# Author: 	Denis Stukal
# Date: 	April 5, 2015
# Summary:	Defines:
#				2 functions for plotting and writing out a .txt file 
# 				a function to check correctness of user's input
# 				the InstrumentsReturns class for simulating daily returns of an investment instrument.
# 			The module contains all necessary elements to simulate daily returns for the investment instrument. 
########################################################################################## 


import numpy as np
import matplotlib.pyplot as plt
import re
import sys
import inputHandler
import simulationFunctions

def plotResults(objectToPlot):
    '''
    Takes an input of dictionary type and saves a histogram in the working directory. 
    '''
    if isinstance(objectToPlot, dict):
        for key in objectToPlot:
            plt.figure() # makes and activates a new figure window
            plt.hist(objectToPlot[key],100,range=[-1,1])
            plt.title('%s investments of %d dollars' % (key, 1000/int(key)))
            plt.savefig('histogram_'+'{0:0>4}'.format(key)+'_pos.pdf')
    else:
        print "This function was designed to be used with inputs of dictionary type. Sorry."
 

def writeOutResults(results):
    '''
    Takes an input of dictionary type and saves a .txt file with the dictionary contents in the working directory.
    '''
    if isinstance(results, dict):
        out = open('results.txt', 'w')
        out.write('Number of investments and the corresponding daily returns means and standard deviations:\n')
        for key in results:
            out.write(key + ': mean = %.3f; sd = %.3f\n' %(np.mean(results[key]), np.std(results[key])))
        out.close()
    else:
        print "This function was designed to be used with inputs of dictionary type. Sorry."


def checkInputDenominations(arg):
    '''
    Function to be used in InstrumentsReturns class to check if the input (positionValues) refer to allowed denominations
    '''
    output = True
    for element in arg:
        if element not in [1, 10, 100, 1000]:
            print "Sorry, only $1, $10, $100, and $1000 denominations are allowed"
            sys.exit(0)


class InstrumentsReturns:
    '''
    Summary: 
        Attributes and functions to simulate daily returns from financial instruments. 
    Attributes: 
        self.totalInvestment (default = 1000)
        self.numTrials (default = 10 000)
        self.positions
        self.positionValue - values to represents the size of each investment
        self.simulationResults - dictionary with results of simulations
    High-level functions:
        getUserInput()
        inputToInteger()
        investmentSize()
        simulate()
        produceResults()
    Low-level functions:
        createStorageObject()
        storeSimulationResults() - inside simulate()
    '''

    def __init__(self):
        '''
        Initializes an instance with all 5 attributes defined in the class. 
        '''
        self.totalInvestment = 1000
        self.numTrials = 10000
        # Call for user input and convert it to a list of integers
        self.positions = self.inputToInteger(self.getUserInput())
        checkInputDenominations(self.positions)
        
        # Get values to represents the size of each investment
        self.positionValue = self.investmentSize(self.positions)
        
        self.simulationResults = self.simulate(self.numTrials)
       


    def getUserInput(self):
        '''
        Asks for user input. No arguments. 
        '''
        try:
            return raw_input("Give the number of shares to buy $1000 in parallel (use commas to separate input): ")
        except KeyboardInterrupt:
            print "\nSorry, you interrupted program execution."
            sys.exit(0)


    def inputToInteger(self, someString):
        '''
        Takes a string as input. 
        Calls noBracketsInInput() and stringToIntegerInInput().
        Returns a list of integers after splitting the input by comma. 
        '''
        stringCleaned = inputHandler.noBracketsInInput(someString)
        return inputHandler.stringToIntegerInInput(stringCleaned.split(','))
    
    
    def investmentSize(self, arg):
        '''
        Takes a list representing chunks of money. Returns a list representing sizes of investment. 
        '''
        output = []
        for element in arg:
            output.append(1000 / element)
        return output
 

    def simulate(self, numTrials):
        '''
        Input:
            integer = number of simulation trials
        Summary:
            Creates a dictionary called 'results' to store results of simulations. 
            Computes daily return for every simulation and stores the results.
        Output:
            dictionary with results of simulations
        '''
        results = self.createStorageObject()
        for trial in range(numTrials):
            cumulativeReturn = simulationFunctions.cumuRet(self.positionValue)
            dailyReturn = simulationFunctions.dailyRet(cumulativeReturn)
            self.storeSimulationResults(results, dailyReturn)
        return results
      
        
    def createStorageObject(self):
        '''
        Creates a dictionary of lists to store simulation results. 
        '''
        results = {}
        for i in range(len(self.positions)):
            results[str(self.positions[i])] = []
        return results
     
    
    def storeSimulationResults(self, stroringObject, dailyReturn):
        '''
        Input:
            stroringObject (dictionary of lists produced by createStorageObject()
            dailyReturn (list of daily returns)
        No output. Changes stroringObject.
        '''
        for i in range(len(self.positions)):
            stroringObject[str(self.positions[i])].append(dailyReturn[i])
 
    
    def produceResults(self):
        '''
        Calls plotResults() and writeOutResults() to write out simulation results
        '''
        plotResults(self.simulationResults)
        writeOutResults(self.simulationResults)
    
 

