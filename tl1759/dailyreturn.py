#############Liwen Tian
############Assignment

##################this module calculates the returns for both cumu_ret and daily_ret###############

from ins import instrument
import numpy as np 


##################fucn returns calculate the returns for both cumu_ret and daily_ret###############
def returns(instrument):
	cumu_ret = {}
	daily_ret = {}
	# num_trial = int(raw_input('please choose a number'))
	# num_trial = 10000 ####Given the assignment, the number_trial is 100000
	for trial in range(0,instrument.trial):
		DoubleValue = []
		position = instrument.investment/instrument.denomination
		for i in range(0,position):
			num = np.random.rand()
			if num <(0.51)or num== (0.51):
				DoubleValue.append((1000/position)*2)
			else:
				pass

		z = sum(DoubleValue)
		cumu_ret[trial] = z
		daily_ret[trial] = (z/1000.0)-1
	return daily_ret,cumu_ret
