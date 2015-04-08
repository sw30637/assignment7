# Name: 	inputHandler.py
# Author: 	Denis Stukal
# Date: 	April 5, 2015
# Summary:	Module contains functions to clean and parse user's input.
# 			 
########################################################################################## 

import re
import sys

def noBracketsInInput(someString):
    '''
    Takes a string as input. Returns a string with no brackets. 
    '''
    return re.sub(r'\[+|\]+|\(+|\)+', '', someString)
    
    
def stringToIntegerInInput(arg):
    '''
    Takes a list or tuple of string representations of numbers. 
    Returns a list of numbers. 
    '''
    try:
        output = []
        for element in arg:
            element = int(element)
            output.append(element)
        return output
    except ValueError:
        print "Error! Non-integer input or integers not separated by commas."
        sys.exit(0)
     