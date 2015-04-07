import sys

def GetUserInput():

	try:
		return raw_input("Input the positions you want the investement to be calculated as in the form of a list: ")

	except KeyboardInterrupt:
		print "\nSorry, you interrupted program execution."
	        sys.exit(0)

def CheckUserInput():
	
	position      = GetUserInput()
	position_list = []

	numbers = position[1:-1].split(',')
	
	try:
		for number in numbers:
			position_list.append(int(number))
	except:
		print "Error! You must input [1,10,100,1000]"
		GetUserInput()

	if [1,10,100,1000] not in position_list:
		return "Error! You must input [1,10,100,1000]"
	else:
		return position_list



