##############Liwen Tian ############
############Assignment_7##########
############################################################################
#############This is the module that draws the histograms and dump the result####


from ins import instrument
from dailyreturn import returns
import numpy as np 
import matplotlib.pyplot as plt
import sys

###############Function output() give the histograms and result.txt##########
def output():
	myfile = open('result.txt', 'w')
		
	usergive= raw_input('Please give a list of the number of shares you want to buy:'+'\n'+
		'(Hint:There must be a space after each position, like [1, 10, 100, 1000]) :')
	# num_trials = raw_input('Set the trial number to get the satistics information')
	positions = []
	try: 
		position_str = usergive[1:-1].split(', ')
		for ele in position_str:
			positions.append(int(ele))

	except ValueError:
		raise Exception('Opps..Please make sure to put in right position.')
	giventrial = raw_input('Give the number of trials you want: ')
########if the user type in 'q', 'Q', or 'Quit' or 'quit', then just exit the process####

	if giventrial == 'q' or giventrial =='Q' or giventrial =='Quit' or giventrial=='quit':
		
		sys.exit()	
		
	else:
		try:
			num_trials = int(giventrial)

		except ValueError:
			raise Exception('Please make sure it is a number')
			sys.exit()


	for ele in positions:
		x = []
		x_value = []
		investment = instrument(ele,1000,num_trials)
		ret = returns(investment)
		daily_ret = ret[0]
		cumu_ret = ret[1]
		for key,value in daily_ret.items():
			x.append(value)
		for key,value in cumu_ret.items():
			x_value.append(value)
		printmean = 'For position_'+str(ele)+' the expected value of daily return is $'+str(np.mean(x_value))+'.'
		printstd =  'The standard deviation is '+ str(np.std(x_value))+'.'
		printstr = printmean +'\n'+printstd+'\n'
		title = "histogram_" + str(ele) +"_pos.pdf"
		plt.hist(x,100,range=((-1.0),1.0))
		plt.xticks(np.arange(-1,1.5,0.5))
		plt.savefig(title)
		plt.close()
		myfile.write(printstr)
	myfile.close()
	print ('The result is in the folder,please go check it.')
	return  ('This is the function draw the histograms.')


