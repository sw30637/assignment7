# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  errorHandler.py 
#  April 3,2015
#
#  Handles errors from inputs of assignment7.py
#
###################################



import sys


class errorHandlerClass():
  def __init__(self, thisError):  
       self.thisError = thisError
      
  def errorHandlerFunction(self, thisError):
    if thisError ==  IndexError:  #in case of IndexError
        print "*"*30
        print "You are too advance. Index is out of range."
        print "*"*30
        sys.exit(1)

    elif thisError ==  ValueError:  #in case of ValueError
        print "*"*30
        print "You are too advance. Please type in valid value next time"
        print "Input will only take a list integer numbers separated by comma"
        print "*"*30
        sys.exit(1)
        
    elif thisError ==  NameError:  #in case of NameError
        print "*"*30
        print "You are too advance. Please use correct name"
        print "*"*30
        sys.exit(1)

    elif thisError ==  KeyboardInterrupt:   #in case of CTRL + C
        print "*"*30
        print "Yo, homie.  Stop messing with keyboard"
        print "*"*30
        sys.exit(1)
        
    elif thisError ==  "shortString":    
        print "*"*30
        print "Input was too short"
        print "*"*30
        sys.exit(1)
        
    elif thisError ==  "listError":
        print "*"*30
        print "Input was not in a list"
        print "*"*30
        sys.exit(1)
        
    elif thisError ==  "overLimit":
        print "*"*30
        print "You can only invest $1000 or less"
        print "*"*30
        sys.exit(1)
        
    elif thisError ==  "negative":
        print "*"*30
        print "Negative value can not be used"
        print "*"*30
        sys.exit(1)

    elif thisError ==  "noZero":
        print "*"*30
        print "Trial has to be one or greater"
        print "*"*30
        sys.exit(1)
        
    elif thisError == SystemExit:
        sys.exit(1)
        
    else:
        print "Undefined Error", thisError
 