# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  assignment7.py 
#  April 3,2015
#
#  "investment instrument" -  Simulation to determine how to make that investment 
#
###################################


import numpy as np
import matplotlib.pyplot as plt
import sys
from errorHandler import errorHandlerClass

def inputReceiver(position_value, num_trials):  
    """
    Receives the number of shares  
    """
    print "Please type in a list of the number of shares to buy in parallel:"
    print "e.g. ​[1, 10, 100, 1000]: "
    
    try: 
        positions = raw_input("---->")
        positions = positionChecker(positions)      #check input
        num_trials = int(input("Please type in number of trials you want to run: "))
        num_trials = numTrialChecker(num_trials)    #check number
        for item in positions:
             eachPosition =  int(item)                 
             position_value[eachPosition] = 1000/eachPosition  #10 will have 100 position
        return position_value, num_trials
    except:
        thisError = sys.exc_info()[0]
        error = errorHandlerClass(thisError)
        error.errorHandlerFunction(thisError)
        
        
def positionChecker(positions):  
    """
    Checks incorrect inputs and returns input as a list 
    """
    positions = str(positions).strip("[").strip("]").replace(" ", "")
    positions = positions.split(",")
    if positions==['']:
        error = errorHandlerClass("shortString")
        error.errorHandlerFunction("shortString")
    else: 
      for item in positions:
        if int(item) >1000:
            error = errorHandlerClass("overLimit")
            error.errorHandlerFunction("overLimit")
        elif int(item) < 0:
            error = errorHandlerClass("negative")
            error.errorHandlerFunction("negative")
      return positions
        
        
def numTrialChecker(num_trials):  
    """
    Make sure the list is 1 or greater
    """
    try:
        num_trials = int(num_trials)     
        if num_trials <1:
            error = errorHandlerClass("noZero")
            error.errorHandlerFunction("noZero") 
        return num_trials
    except:
        thisError = sys.exc_info()[0]
        error = errorHandlerClass(thisError)
        error.errorHandlerFunction(thisError)   

        
        
def investmentFolder(position_value, num_trials):
    """
    Receives position value, send the value for calculation, and send the return for output
    """
    portfolio={}        
    for key, value in position_value.items():
        portfolio[key] = calculator(key, value, num_trials)    #builds portfolio dictionary
    output(portfolio)
        
       
    
def calculator(key, value, num_trials):
    """
    Calculation of returns
    """
    tran_ret={}   #per transaction
    cumu_ret={}   #per trial
    daily_ret={}  #per day 
    trial = 0
    for num in xrange(num_trials):
        thisSum = 0
        for item in xrange(value):
            odd =  np.random.multinomial(1, [.51, .49])[0]
            result = odd * key
            if result == 0:
                tran_ret[item] = 0
            else:
                tran_ret[item] = result+key
            thisSum += float(tran_ret[item])
            cumu_ret[num]=thisSum
        trial=num+1
        daily_ret[trial] = round((cumu_ret[num]/1000.)-1, 2)
    return daily_ret
    
    
def output(portfolio):
    """
    Output
    """
    printer={}
    for key, value in portfolio.items():
        X=[]
        for subkey, subvalue in value.items():
           X.append(subvalue)
        std = np.std(X)     #standard deviation 
        mean = np.mean(X)   #average
        printer[key]=std, mean    
        
        plt.figure()
        plt.hist(X, 100, range=[-1,1]) 
        plt.xlabel("The probability to win or lose")
        plt.title('thk301 - The histogram of the result $%s' %key)
        plt.ylabel('The number of trials')
        plt.autoscale(False, tight=True)
        if key==1000:
            plt.savefig('histogram_1000_pos.png')
        elif key==100:
            plt.savefig('histogram_0100_pos.png')
        elif key==10:
            plt.savefig('histogram_0010_pos.png') 
        elif key==1:
            plt.savefig('histogram_0001_pos.png')
        else:
            plt.savefig('histogram_%s_pos.png' %key) 
            
    file = open("results.txt", "w")        #save the "printer" dictionary
    for key, value in printer.items():
       file.write( "$%d\n" %key)
       file.write("Standard Deviation:%f\n"%value[0])
       file.write( "Mean:%f\n\n"%value[1])

     
if __name__ == "__main__":
    position_value = {}
    num_trials = 0
    position_value, num_trials = inputReceiver(position_value, num_trials)
    investmentFolder(position_value, num_trials)


