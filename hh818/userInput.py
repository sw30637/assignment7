'''
Created on Apr 8, 2015

@author: ds-ga-1007
'''
def inputPositions():
    while True:
        try:
            positions = raw_input("a list of numbers of shares to buy").split(", ")
            positions = [int(position) for position in positions]
            for position in positions:
                if position < 1:
                    raise Exception("invalid input, number must be positive integers")
                else:
                    return positions
                    break
                
        except:
            print("invalid input")
            
def inputNum_trial():
    while True:
        try:
            num_trial = int(raw_input("how many times to randomly repeat the test"))
            
            if num_trial < 1:
                print("invalid input, number must be positive integers")
            else:
                return num_trial
                break
        except:
            print("invalid input, number must be positive integers")