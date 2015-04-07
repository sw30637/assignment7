import numpy as np
import sys
import matplotlib as plt

import investsim as inv


#Prompt for user input
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
	thous.append(inv.returns(1000, shares_at_thousand))
	hund.append(inv.returns(100, shares_at_hundred))
	ten.append(inv.returns(10, shares_at_ten))
	one.append(inv.returns(1, shares_at_one))
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