##########################Author: Liwen Tian

################Assignment_7
#######################################################################################
###This module define a class called instrument, which is an investment instrument##### 
###and the class has attributes like denomination,total_investment
### and the method like onetrial_return, returns#########
import numpy as np 

class instrument:
########################this are the attributes of the class##############################
	def __init__(self,denomination,total_investment,num_trials):
		self.denomination = denomination
		self.investment = total_investment
		self.trial = num_trials
#######################################################################################
##########This is the print of the class#######################
	def __str__(self):
		return 'denomination: '+str(self.denomination)+'\n'+'total_investment: '+str(self.total_investment)
		self.investment = total_investment
#######################################################################################

	
