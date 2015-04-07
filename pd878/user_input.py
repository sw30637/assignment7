'''
Created on Apr 5, 2015

@author: Pan Ding pd878package@nyu.edu
'''
import sys

total_investment = 1000

def take_positions():
    '''Lets user input number(s) of shares to buy in paralle.'''
    while True:
        try: 
            num_shares = raw_input('Enter number(s) of shares to buy in paralle, i.e. positive integer divisors of 1000, separated by comma (e.g. 1, 10, 1000): ').split(',')
            positions = [int(n) for n in num_shares]
            if is_positive_divisor(total_investment, positions) == True:
                return positions
            else:
                raise ValueError 
        #catches invalid input    
        except ZeroDivisionError:
            print "\nOops!  Invalid input."
        except ValueError:
            print "\nOops!  Invalid input."
        except KeyboardInterrupt:
            print 'You pressed Ctrl+C! Exiting...'
            sys.exit()    

def take_num_trials():
    '''Lets user input number of trials'''
    while True:
        try:
            num = raw_input('Enter number of trials (a positive integer): ')
            num_trials = int(num)
            if num_trials > 0: # checks if the input is positive
                return num_trials
            else:
                raise ValueError 
        #catches invalid input    
        except ValueError:
            print "\nOops!  Invalid input."
        except KeyboardInterrupt:
            print 'You pressed Ctrl+C! Exiting...'
            sys.exit()

def is_positive_divisor(number, list_integers):
    '''Takes a number and a list of integers, 
    check if the list of integers are positive divisors of the number'''
    return all(number%i == 0 and i >0 for i in list_integers)
