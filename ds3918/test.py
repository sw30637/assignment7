# Title: 	test
# Author: 	Denis Stukal
# Date: 	April 5, 2015
# Summary: 	Tests for assignment 7. 
####################################################################

import unittest
import os


class testsForInvestment(unittest.TestCase):
    '''
    Defines 2 tests: if plots and the results.txt file exit in the working directory
    '''
    def test_plots(self):
        self.assertTrue(os.path.exists('histogram_0001_pos.pdf'))
        self.assertTrue(os.path.exists('histogram_0010_pos.pdf'))
        self.assertTrue(os.path.exists('histogram_0100_pos.pdf'))
        self.assertTrue(os.path.exists('histogram_1000_pos.pdf'))
    
    def test_results_txt(self):
    	self.assertTrue(os.path.exists('results.txt'))
        

if __name__ == '__main__':
	unittest.main()


