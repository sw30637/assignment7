'''
Created by: Joseph Song (JLS731)
Assignment #7
Description: This is the unittest to test the functions and classes of the package to make sure that the output
is in the correct form
'''
import unittest
import numpy as np

from investmentDetails import *
from ProduceOutput import *
from RunSimulations import *

class Test(unittest.TestCase):


    def testInvestmentDetailsClass(self):
        '''Test to make sure we get the correct and values'''
        self.test_string = '[2,5,10,50]'
        self.test_array = investmentDetails(self.test_string)
        self.correct_array = np.array([2,5,10,50])
        self.correct_values = np.array([500,200,100,20])
        
        self.assertTrue((self.test_array.num_shares==self.correct_array).all(),"Incorrect Array")
        self.assertTrue((self.test_array.position_value==self.correct_values).all(),"Incorrect Array")
    
    def testRunSimulations(self):
        '''Test the output of the simulation results'''
        self.positions = np.array([1,10,100,1000])
        self.value = np.array([1000,100,10,1])
        
        self.sim_results = runSimulation(self.positions, self.value, 10)
        self.assertEqual(self.sim_results.shape, (4,10), "The shape of the array is incorrect")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()