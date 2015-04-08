'''
A module that contains the code for assignment 7 that accepts input on positions and trials from the user. 

Created on Mar 31, 2015
@author: Adam Biesenbach
'''

from PositionsClass import position
from PositionsClass import PositionsException
from TrialsClass import TrialException
from TrialsClass import trial
import sys 

def ReturnUserInput():
    """ A master function that returns a lists of intervals with a new interval inserted in."""
    # From an initial list provided by the user, handle error to make sure that the intervals are valid.

    return (ValidatePositions(), ValidateTrials())
    
def ValidatePositions():
    '''Here is a function to handle exceptions to the positions list.'''

    # Get input from the user. If the string is empty, prompt them again.
    # If not, take out each of the parsed elements and try to put it into the position class.
    # If an exception is raised, add it to the exceptions list. If after running the loop,
    # the length of the errors list is greater than zero, prompt again.
    
    while True:
        InitialPositions = GetUsersInitialPositions()        
        if InitialPositions !="":
            try:
                PoisitionClassInstance = position(InitialPositions)
                break
            except PositionsException:
                print "Invalid positions."
            except ValueError:
                print "Invalid positions."
        else:
            print "Invalid positions."
            continue
    return PoisitionClassInstance

def GetUsersInitialPositions():
    """Return the raw input from the user containing the initial list of positions."""
    try:    
        InitialPositions = raw_input("List of Positions? ")
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
    else: 
        return InitialPositions

def ValidateTrials():
    while True:
        InitialTrials= GetUsersNumbersOfTrials()        
        if InitialTrials !="":
            try:
                trialClassInstance = trial(InitialTrials)
                break
            except TrialException:
                print "Invalid trial." 
        else:
            print "Invalid trial."
            continue
    return trialClassInstance

def GetUsersNumbersOfTrials():
    """Return the raw input from the user containing the number of trials."""
    try:
        Trials =  raw_input("Numbers of trials? ")
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
    else: 
        return Trials 
