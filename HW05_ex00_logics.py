#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
	""" Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
	returns None"""

	input_value = raw_input("Enter a number: ")
	try:
		input_num=int(input_value)
	except:
		print "Only numbers, please start over"
	else:
		if (input_num % 2 == 0):
			print ("Even")
		else:
			print("Odd")
		

def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    for i in range (1,101):
		if (i%10 == 0):
			print '\t',i,'\n'
		else:
			print '\t',i,
			
def find_average():
	""" Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
	sum=0
	n=0
	check = True
	while check:
		input_value = raw_input("Input a number")
		if input_value != "done":
			try:
				input_normalize = float(input_value)
			except:
				print "Please enter a numeral or done"
			else:
				sum = sum + float(input_value)
				n = n+1
		else:
			if n == 0:
				print "Please enter a number and start over"
			else:
				check = False
				return (sum/n)
				
			 
			
##############################################################################
def main():
	""" Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
	#even_odd()
	#ten_by_ten()
	print find_average()
	

if __name__ == '__main__':
    main()
