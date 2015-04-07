'''
This module creates a class that represents the list of positions generated by the user. It does
error handling to ensure that the input form the user conforms to the requirements of the question.

Created on Mar 31, 2015
@author: Adam Biesenbach
'''

import re

# Create a new class for handling positions errors.
class PositionsException(Exception): pass

class position:
    """A class that represents the a list of positions."""

    #this next bit defines the 'constructor.' and the objects which are accessible when the class is initialized.
    def __init__(self, Positions):
        
        self.Positions = str(Positions)
        
        # Pull out the numbers in the range.
        self.SplitPositions = self.Positions[1:-1].split(",")      
        
        # In this section, I do some error testing to make sure that the user is feeding the right kind of input.
        
        def NotAListHandling():
            """Test to ensure that they submit a properly formatted list."""
            if self.Positions[0]!="[" or self.Positions[-1]!="]":
                raise PositionsException("Positions not given in list.")
            for element in self.SplitPositions:
                try:
                    self.SplitPositionsFinal = [float(element) for element in self.SplitPositions]
                except ValueError:
                    raise PositionsException("Invalid positions.")
                
        def EmptySetHandling():
            if self.SplitPositions ==[]:
                raise PositionsException("Empty position list.")
            
        def ImproperPositionsHandling():
            """ if the positions are not either 1, 10 , 100 or 1000, throw an exception."""
            NumberOfErrors = [] 
            for element in self.SplitPositionsFinal:
                if element!=1 and element!=10 and element!=100 and element!=1000: 
                    NumberOfErrors.append(element)
                if len(NumberOfErrors)>0:
                    raise PositionsException("Positions must be in $1, $10, $100, or $1000 denominations.")

        NotAListHandling()        
        EmptySetHandling()
        ImproperPositionsHandling()
        
        self.PositionsInList = [int(x) for x in  self.SplitPositionsFinal]
            