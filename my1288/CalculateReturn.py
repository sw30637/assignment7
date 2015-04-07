import numpy as np
import matplotlib.pylab as plt

# Create a class which will handle all the investment return calculations
class InvestmentTrials:

	def __init__(self, positions, num_trials, total_investment):
		self.positions 	 = positions
		self.trials  	 = num_trials
		self.investment  = total_investment

	def CalculateTrials(self):


		text_file = open("results.txt", "w")
		
		text_file.write("The following are the calculation results: \n")

		# iterate through the list of positions to get the investment for each
		for position in self.positions:
			
		
			# initialize the arrays that will contain the final results
			cumu_ret    = np.zeros(self.trials)
			daily_ret   = np.zeros(self.trials)
			

			# Calculate the investment position
			position_value = self.investment/float(position)

			# Carry out each trial
			for trial in range(self.trials):
				one_ret     = []
				# for each position 
				for num in range(position):
					# generate a random number and compare
					random_prob = np.random.rand()
					if random_prob >= .49:
						one_ret.append(position_value*2.0)
					else:
						one_ret.append(0)

				# Sum up the trials for each position to get the total return
				cumu_ret[trial] = sum(one_ret)

			# Normalize the daily return
			daily_ret = (cumu_ret/1000.0)-1
			
			# Set the filename for the pdf of each position
			filename = 'histogram_'+ str(position) + '_pos.pdf'
			
			# Plot the results
			plt.hist(daily_ret, 100, range = [-1,1])
			plt.savefig(filename)
			plt.clf()
			plt.close()
			
			# Send the values for mean and std dev to a txt file
			text_result = str(position) + ": Mean = " + str(np.mean(daily_ret)) + ", Std Dev = " + str(np.std(daily_ret)) + "\n"
			text_file.write(text_result)

			


		text_file.close()

	





