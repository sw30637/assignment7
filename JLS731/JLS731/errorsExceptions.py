'''
Created on Mar 18, 2015
Created by Joseph Song (JLS731)
These exceptions capture specific errors rather than using catchall
'''


class incorrectInputException(Exception):
    """ Raises error message when interval input is incorrect """
    def __str__(self):
        return 'Invalid Inputs - Values need to be integers, separated by commas, closed by square brackets (e.g [1,10,100])'  
    