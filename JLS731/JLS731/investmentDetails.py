'''
Created by: Joseph Song (JLS731)
Assignment #7

Description: This is the investment class which holds the
number of shares (positions) and value of each share and raises an
exception when the input is not an integer
'''

from types import *
from errorsExceptions import *
import numpy as np

class investmentDetails:
    '''investment class: Creates the details (positions and position_values) '''
    def __init__(self, positions):
        '''Take the string input and turn it into an array of numbers'''
        try:
            leftBrace = positions[0]
            positionValues = positions[1:-1]
            rightBrace = positions[-1]
        except:
            raise incorrectInputException()        
        
        try:
            assert leftBrace in ["["]
            assert rightBrace in ["]"]
            positionListTemp = positionValues.split(',')
            positionList = np.zeros(len(positionListTemp), dtype=np.int)
            for i in range(len(positionListTemp)):
                'Make sure that the positions are an integer, less than 1000 but not 0 or negative'
                assert(float(positionListTemp[i])==int(positionListTemp[i]))
                positionList[i] = int(positionListTemp[i])
                assert(positionList[i]<=1000)
                assert(positionList[i]!=0)
            self.num_shares = positionList
            self.position_value = 1000./self.num_shares
        except:
            raise incorrectInputException()

        
    def __repr__(self):
        '''Spit out the number of shares'''
        return str(self.num_shares)
