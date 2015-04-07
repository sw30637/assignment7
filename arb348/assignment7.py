'''
This is programming for Assignment 7. This is the main program which will 
generate my answers for the assignment, which deals with programming in NumPy.
Each of the questions from the assignment has its own module, and from each module 
we import the function responsible for generating the required output. In addition, I 
performed some unit testing of the functions used to generate the results displayed here. 


Author: Adam Biesenbach
Date: March 31, 2015
'''
from GenerateReturns import GenerateDailyReturns
from AcceptInputFromUser import ReturnUserInput
from PlotHistograms import PlotHistograms
from NumericalResults import CreateNumericalResults
import sys 

if __name__ == '__main__':
 
    try:    
        # Return the input from the user, which are the positions and number of trials. 
        (positions, num_trials) = ReturnUserInput()
    
        # Generate the series that the assignment asks for, which are the cumulative returns
        # on the days for the different investment decisions and the daily    
        (cumu_ret, daily_ret) = GenerateDailyReturns(positions, num_trials)
        
        # If we get the input specified by the assignment, generate the pdfs and text file. 
        if positions.PositionsInList==[1,10,100,1000] and num_trials.TrialNumber==10000:  
            CreateNumericalResults(cumu_ret, daily_ret)
            PlotHistograms(daily_ret)
                
    except KeyboardInterrupt:
        print "\n whoops... KeyboardInterrupt... exiting program."
        sys.exit(0)
            
       
