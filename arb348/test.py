'''
Created on Mar 31, 2015
@author: Adam Biesenbach

This file contains tests for the functions used to answer assignment #7. 
'''
import unittest
import os.path
from PositionsClass import position
from TrialsClass import trial
from GenerateReturns import GenerateDailyReturns
import numpy as np 

class TestAssignment7Functions(unittest.TestCase):
    """This class provides the structure for the unit testing we perform for each
    function responsible for creating the answers to Assignment 7."""
      
    def testMeans(self):
        """test that the means are reproduced correctly."""
        self.testPositions = position("[1,10,100,1000]")
        self.testTrials = trial("10000")
        self.assertTrue(-1<=np.all(GenerateDailyReturns(self.testPositions, self.testTrials)[1])<=1, "Daily returns series has incorrect values.")
      
    def testFilesExist(self):
        """ Test to ensure that the output file exist."""
        self.assertTrue(os.path.exists("./histogram_0001_pos.pdf"), "A histogram didn't save to output.")
        self.assertTrue(os.path.exists("./histogram_0010_pos.pdf"), "A histogram didn't save to output.")
        self.assertTrue(os.path.exists("./histogram_0100_pos.pdf"), "A histogram didn't save to output.")
        self.assertTrue(os.path.exists("./histogram_1000_pos.pdf"), "A histogram didn't save to output.")
        self.assertTrue(os.path.exists("./results.txt"), "Results file doesn't exist.")

if __name__ == "__main__":
  
    unittest.main()