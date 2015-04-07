# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  unittest7.py 
#  April 4,2015
#
#  1. testing array is correctly built
#  2. testing listMaker returns correct list
#  3. testing values of problem 3 are equal
#
###################################

import unittest
import assignment7 as a7
from errorHandler import errorHandlerClass

class Assignment7Test(unittest.TestCase):

    def setUp(self):
        print "setUp"
    
    def testCalculator(self):
        result = a7.calculator(1,2,3)
        for key, value in result.items():
            self.assertEqual(abs(value), abs(1))  #either 1 or -1
        
    def testPositionChecker(self):   #make sure a space is not an issue
        self.assertEqual(a7.positionChecker("[1,       100]"), ['1', '100'])
        self.assertEqual(a7.positionChecker("[1,10,      100]"), ['1', '10', '100']  )
        self.assertEqual(a7.positionChecker("[       5,  10,      100   ]"), ['5', '10', '100'] )
        self.assertEqual(a7.positionChecker("[       10,         100,      1000     ]"), ['10', '100', '1000'] )
        
        
if __name__ == '__main__':
   unittest.main()
   
   