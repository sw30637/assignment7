#####################################################
#													#
#	DS-1007 Programming for Data Science			#
#	Assignment 7									#
#													#
#	Lily Fung										#
#	April 7, 2015									#
#													#	
#	Investment Simulation Module					#
#	Objecive: To estimate returns on a near-50-50	#
#	risk investment 								#
#####################################################

import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def investment_options(shares, shares_at_hundred, shares_at_ten, shares_at_one):
	positions = [shares_at_thousand, shares_at_hundred, shares_at_ten, shares_at_one]
	return positions

# The function returns(shares, position_value) takes two arguments, position_value and shares.
# Position value can be $1000, $100, $10, or $1 and shares is number of shares in that order.
def returns(position_value, shares):
	
	#binary_simulator is an array of 0s and 1s, for the number of shares held at that value.
	binary_simulator = np.random.choice(2, shares, p=[0.49, 0.51])
	
	#cumulate_returns is the return from investment, initialized at 0
	cumulate_returns = 0 

	#for each 0 or 1 in the binary_simulator array, increment cumulate_returns by 0 or 1 times the $2000/$200/$20/$2 prize.
	for win_or_loss in binary_simulator:
		cumulate_returns += win_or_loss*2*position_value

	return cumulate_returns

class investment_choices(object):
	def __init__(self, input_list):
		self.shares_of_1000 = input_list[0]
		self.shares_of_100 = input_list[1]
		self.shares_of_10 = input_list[2]
		self.shares_of_1 = input_list[3]
	def __repr__(self):
		return [self.shares_of_1000, self.shares_of_100, self.shares_of_10, self.shares_of_1]



######################################Code##############################

shares_at_thousand = int(raw_input("How much would you like to invest? (Must be in increments of 1,000) \n"))/1000

# try:
# 	int(shares_at_thousand)%1000
# 	break
# except ValueError:
# 	print "That is not a multiple of 1,000. Sorry, try again!"

shares_at_hundred = shares_at_thousand*10
shares_at_ten = shares_at_thousand*100
shares_at_one = shares_at_thousand*1000

num_trials = int(raw_input("How many different single days of trading should we simulate? \n"))

#Initialize trial number, a variable to be incremented after every trial, and four arrays to contain the trial results and plot
trial = 0

thous = []
hund = []
ten = []
one = []

while trial < num_trials:
	thous.append(returns(1000, shares_at_thousand))
	hund.append(returns(100, shares_at_hundred))
	ten.append(returns(10, shares_at_ten))
	one.append(returns(1, shares_at_one))
	trial += 1

mean_string = "Expected Value of Daily Return \n" + " $1000 Per Share: " + str(np.mean(thous)) + "\n $100 Per Share: " + str(np.mean(hund)) + "\n $10 Per Share: " + str(np.mean(ten)) + "\n $1 Per Share: " + str(np.mean(one))

std_string = "Standard Deviation \n" + " $1000 Per Share: " + str(np.std(thous)) + "\n $100 Per Share: " + str(np.std(hund)) + "\n $10 Per Share: " + str(np.std(ten)) + "\n $1 Per Share: " + str(np.std(one))

results = open("results.txt", "w")
results.write(mean_string + "\n" + std_string)
results.close()

fig, ((ths, hun), (tns, ons)) = plt.subplots(nrows=2, ncols=2, sharey=False, sharex=True)

ths.set_title("$1000 Per Share")
ths.hist(thous, 2)

hun.set_title("$100 Per Share")
hun.hist(hund, 10)

tns.set_title("$10 Per Share")
tns.hist(ten, 20)

ons.set_title("$1 Per Share")
ons.hist(one, 30)

fig.suptitle("Histogram of Simulation Results for Single Day of Trading")
plt.show()

# pp = PdfPages('histograms_all.pdf')
# pp.savefig()