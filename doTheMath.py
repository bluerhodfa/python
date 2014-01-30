#!/usr/bin/env python -tt

''' 
Python times table program

    Copyright (C) 2014  Bluerhodfa Consulting Ltd

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''
#Always define all of your functions at the top of your code before the call to main()

def doTheMath(a,t):
	""" Document your functions here then you can remember what they are supposed to do

	Multiplies two int numbers

	Args:
	      int a = a number between 1 and 12
	      int t = a number defining the times table to compute

	Returns:
	      int r = the result of a * t

	Note:
	       You can run the pydoc command on your code to show this documentation

	"""
	r = (a * t)
	return r

def checkInput():
    """ Validate the the user has typed in what you expect to see """
    while True:
    	try:
    		choice = raw_input ('\nPlease enter a number between 1 and 12 to print your times table: ')
    		if int(choice) >= 1 and int(choice) <= 12:
    		    return int(choice)
    		else:
    		     print 'Invalid input!'
    	except ValueError:
    		 print "\nERROR: %s is not a number between 1 and 12, please try again" % (choice)
	    
# The program logic starts here

def main():
    """ Always define a main() function as it is standard coding practice """
    

    print 'Welcome to the times tables generator\n'

# Lets start by checking that we have a number

    choice = checkInput()

# convert the integer number to a string from numbers list

    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

    num2Word = numbers[choice]

    print 'The ' + num2Word + ' times table'

# start at 1 times the selected table

    n = 1

# loop from 1 to 12 and print the table using formatted output

    while (n < 13):
        print ' %d x %d = %d' % (n, choice, doTheMath(n,choice))
        n+=1        

# This is the standard boilerplate way to call the main() function, use it all the time 

if __name__ == '__main__':
	main()