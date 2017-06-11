# ------------------------------------------------------------------------- #

# Question 1
# ------------------------------------------------------------------------- #
def add(a, b):
	"""
	Computes the sum of a and b.

	Args:
		a: addend- float or int to be summed
		b: addend- float or int to be summed

	Returns:
		the sum of a and b
	"""
	# FIXME
	return ________

def sub(a, b):
	"""
	Computes the difference of b from a.

	Args:
		a: minuend- float or int to be subtracted from
		b: subtrahend- float or int to subtract

	Returns:
		the differnce of b from a
	"""
	# FIXME
	return ________

def mul(a, b):
	"""
	Computes the product of a and b.

	Args:
		a: factor- float or int to be multiplied
		b: factor- float or int to be multiplied

	Returns:
		the product of a and b
	"""
	# FIXME
	return ________

def div(a, b):
	"""
	Computes the quotient of a by b.

	Args:
		a: dividend/numerator- float or int to be divided
		b: divisor/denominator- float or int to be divided by

	Returns:
		the quotient of a by b
	"""
	# FIXME
	return ________

def square(x):
	"""
	Computes the square of x.

	Args:
		x: number to be squared

	Returns:
		the square of x
	"""
	# FIXME
	return ________

# ------------------------------------------------------------------------- #

# Question 2
# ------------------------------------------------------------------------- #
def quart(x):
	"""
	Computes the fourth power of x without explicitly writing
	x * x * x * x or sqr(x) * sqr(x). HINT: use a previously
	defined function

	Args:
		x: number to quarted

	Returns:
		the fourth power of x
	"""
	# FIXME
	return ________

def cube(x):
	"""
	Computes the third power of x without explicitly writing
	x * x * x. HINT: use a previously defined function

	Args:
		x: number to quarted

	Returns:
		the third power of x
	"""
	# FIXME
	return ________

# ------------------------------------------------------------------------- #

# Question 3
# ------------------------------------------------------------------------- #
def merge_strings(str1, str2):
	"""
	Makes a new string composed of merging
	the two strings together. HINT: think of
	how to add two strings together

	Args:
		str1: first part of the merged string
		str2: second part of the merged string

	Returns:
		new string which is combo of str1 and str2
	"""
	# FIXME
	return ________

def stringed_out(str0):
	"""
	Makes a list of the first, third, and fifth
	characters in the provided string. HINT: strings
	can be indexed too. Assume the provided string
	will always be at least 5 characters long.

	Args:
		str0: string to be "stringed out"

	Returns:
		list of 1st, 3rd and 5th letters of str0
	"""
	# FIXME
	return ________

def length_of_str(str0):
	"""
	Determines the length of a string.
	HINT: There is a built-in function
	that will help you out a lot here.

	Args:
		str0: string

	Returns:
		the length of the string
	"""
	# FIXME
	return ________

def slice1(str0, start):
	"""
	Makes a string which is just str0 started
	from the character at the start index.

	Args:
		str0: string to slice
		start: number, where to start the new string
			from str0

	Returns:
		a string which is all the characters of str0
		after and including the start index
	"""
	# FIXME
	return ________

def slice2(str0, end):
	"""
	Makes a string which is just str0 from the
	beginning character up to the but not including
	the end index.

	Args:
		str0: string to slice
		end: number, where to end the new string
			from str0

	Returns:
		a string which is all the characters of str0
		before and excluding the end index
	"""
	# FIXME
	return ________

def slice_and_dice(str0, start, end):
	"""
	Makes a string which is str0 started
	from the character at the start index and ended
	at the end index. NO PRIMITIVE OPERATIONS allowed
	in this function i.e. no touching str0 directly
	inside slice_and_dice.

	Args:
		str0: string to slice
		start: number, where to start the new string
			from str0
		end: number, wher to end the new string
			from str0

	Returns:
		a string which is all the characters of str0
		from the start index up to the end index
	"""
	# FIXME
	return ________

def chop_it_up(str0, str1):
	"""
	Make a new string which consists of the first
	half of str0 combined with a space in between
	the second half of str1. HINT: a function from
	a previous question will come in handy here.

	Args:
		str0: former part of new string
		str1: latter part of new string

	Returns:
		a new string which is the combination of
		str0 and str1
	"""
	# FIXME
	return ________

# ------------------------------------------------------------------------- #

# Question 4
# ------------------------------------------------------------------------- #
def powerful_func(lst):
	"""
	Determines the minimum number from the
	1st, 3rd and 5th values of the passed
	in list as well as the minimum number
	from the 2nd, 4th and 6th values of the
	passed in list. Then determines the
	maximum of these two values and squares it.

	Args:
		lst: a list containing at least 6 numbers

	Returns:
		a tuple containing first the min of the 1, 3,
		5 numbers in lst, second the min of the 2, 4,
		6 numbers in lst, third the square of the
		max of these two numbers
	"""
	# FIXME
	first = ________
	second = ________
	return ________

def stretch_func(lst):
	"""
	Creates a list which has the elements of lst
	repeated three times (e.g. [1, 2, 3] --> [1, 2, 
	3, 1, 2, 3, 1, 2, 3]). We then remove the third
	element of the first repetition, the second element
	of the second repetition and the first element
	of the third repetition.

	Args:
		lst: a list containing at least 3 numbers

	Returns:
		a list with at least 6 numbers
	"""
	# FIXME
	lst2 = ________
	lst2.pop(________)
	lst2.pop(________)
	lst2.pop(________)
	return lst2

def quart_and_square(lst):
	"""
	Subtracts the square of the sum of the list
	from the quart of the largest number in the
	list.

	Args:
		lst: a list containing at least 3 numbers

	Returns:
		a tuple containing the string "RESULT" as
		well as the results of our calculations
	"""
	# FIXME
	val1 = ________
	val2 = ________
	return (________, ________)

# ------------------------------------------------------------------------- #

# Question 5
# ------------------------------------------------------------------------- #
def wardrobe(jackets, shoe_brands, shoe_prices):
	"""
	Adds the entry "Ralph Polo": 40 to the provided dictionary.
	Creates a new dictionary with three entries:
	"Nike": 10, "Adidas": 20, "Jordans": 30
	Then creates another dictionary containing two entries:
	"jackets": the provided dictionary, "shoes": the dictionary
	created in this function.

	Args:
		jackets: a dictionary containing jacket brands and prices
		shoe_brands: a three item list of shoe brands
		shoe_prices: a three item list of shoe brand prices

	Returns:
		a tuple with the first value being "Clothes" and the
		second value being a dictionary containing a dictionary
		of jackets and a dictionary of shoes
	"""
	# FIXME
	________
	________
	...
	return {________, ________}

if __name__ == '__main__':
	main()