import unittest
import os

# Create a Unit test file that will check whether the files needed to be generated have been generated

class testsForResults(unittest.TestCase):

	def testCompletePackage(self):

	# Check for all the Histograms	
        	self.assertTrue(os.path.exists('histogram_1_pos.pdf'))
        	self.assertTrue(os.path.exists('histogram_10_pos.pdf'))
       		self.assertTrue(os.path.exists('histogram_100_pos.pdf'))
        	self.assertTrue(os.path.exists('histogram_1000_pos.pdf'))
    	
	# Check for the results.txt
    		self.assertTrue(os.path.exists('results.txt'))
        
	# Check for all the files needed in the Python Package
		self.assertTrue(os.path.exists('CalculateReturn.py'))
		self.assertTrue(os.path.exists('assignment7.py'))
		self.assertTrue(os.path.exists('UserInput.py'))

if __name__ == '__main__':
	unittest.main()
