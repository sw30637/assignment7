# Name: 	simulationFunctions.py
# Author: 	Denis Stukal
# Date: 	April 5, 2015
# Summary:	Module contains function to compute daily returns for the investment instrument.
# 			 
########################################################################################## 

import numpy as np
      
def cumuRet(arg):
    '''
    Input: positionValue (list)
    Summary: returns 0 with p=0.49, returns doubled input value with p=0.51
    Output: list (values corresponding to every element of the arg list)
    '''
    output = []
    for element in arg:
        intermediate = []
        for i in range(1000 / element):
            if np.random.rand() <= 0.49:
                intermediate.append(0)
            else:
                intermediate.append(element * 2)
        output.append(np.sum(intermediate))
    return output

    
def dailyRet(arg):
    '''
    Input: list of daily gains
    Output: list of daily returns
    '''
    output = []
    for element in arg:
        output.append(float(element) / 1000 - 1)
    return output
     

 