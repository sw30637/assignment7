'''
Created by: Joseph Song (JLS731)
Assignment #7
Description: This is the main program to run assignment #7. It takes user input and runs simulations 
of the investment and outputs histograms and the expected value and standard deviations of each
"position" in a .txt file
'''

from investmentDetails import *
from ProduceOutput import *
from RunSimulations import *
from errorsExceptions import *


if __name__ == '__main__':
    
    userInputList = raw_input("Enter a list of the number of shares to buy in parallel:" + '\n')
    while userInputList != "quit":
        'Test that the input of the positions is the correct form'
        try:
            userInputListNoSpace = userInputList.replace(" ", "") #get rid of any whitespace
            listofShares = investmentDetails(userInputListNoSpace)
            userInputNumTrials = raw_input("Enter the number of trials to run:" + '\n') #Number of simulations
            numTrials = 0
            while numTrials == 0:
                'Test that the number of simulations is the correct form'
                try:
                    numTrials = int(userInputNumTrials)
                except EOFError:
                    print("EOF Received: Good Bye")
                except KeyboardInterrupt:
                    print("Keyboard interrupt received: Good Bye")
                except:
                    print 'Not a positive integer, try again'
                    userInputNumTrials = raw_input("Enter the number of trials to run:" + '\n')
            print 'Calculation in progress...'
            sims = runSimulation(listofShares.num_shares, listofShares.position_value, numTrials)
            computeStats(sims, listofShares.num_shares)
            produceHistogram(sims, listofShares.num_shares)
            userInputList = "quit"
        except(incorrectInputException) as e:
            print(e)
            userInputList = raw_input("Try Again: Enter a list of the number of shares to buy in parallel:" + '\n')
        except EOFError:
            print("EOF Received: Good Bye")
        except KeyboardInterrupt:
            print("Keyboard interrupt received: Good Bye")
    print "Results Produced: Good Bye"
    