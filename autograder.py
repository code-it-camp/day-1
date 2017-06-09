import sys
import unittest
from graderlib import test_case

import practice

def run_test(module, question):
	# test is the instance of our TestCase class with all of our
	# desired question, specified by argv[1], functions to be tested.
	test = test_case(module, question, question_inputs)

	# not test corresponds to a requested question test which
	# doesn't exist
	if not test:
		return

	# adds our TestCase to the global attributes so that unittest
	# will find it when it searches for TestCases to run
	globals()[test.__name__] = test

	print()
	print('Question', question[1:])

	"""
	argv='q' allows the program to use the command line arguments
	as the question input. q is a dummy attribute class of __main__
	so that the unittest will run that as the passed in command
	arguments, then our program can access the actual command args
	without them messing up the unittest! DO NOT make the value for
	argv more than one character: no clue why, but the unittest main
	function tries to split the argv value into single characters so
	unless we have each of those individual characters defined as
	dummy attribute classes of __main__ (which there's no reason to
	do so), just leave argv as 'q' be and accept the ludicracy of
	this frickin stupid argument.
	"""
	unittest.main(argv='q')

def main(module):
	# Test all questions.
	if len(sys.argv) == 1:
		for question in question_inputs:
			run_test(module, question)
	# Test one specific question specified
	# by the single argument passed in.
	elif len(sys.argv) == 2:
		run_test(module, sys.argv[1])
	# Too many arguments.
	else:
		print("Too many arguments. Check the README.md "
			+ "for proper formatting of question tests.")

"""
Dictionary of allowed question test requests
	Dictionary of functions in practice part
	of this question test
		Function to be tested: list of lists
		which correspond to a test input for
		this function and an expected output
"""
question_inputs = {
	"q1": {
		"add": [
			[(2, 3), 5],
			[(9, 8), 17]
		],
		"sub": [
			[(23, 2), 21],
			[(90235, 12838), 77397]
		],
		"mul": [
			[(13, 20), 260],
			[(24, 12), 288]
		],
		"div": [
			[(56, 8), 7],
			[(84, 7), 12]
		]
	}
}

if __name__ == '__main__':
	main(practice)
