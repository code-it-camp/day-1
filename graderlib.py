from re import match
import unittest

def test_case(module, question, question_inputs):
	"""
	Determines if grader has been given a valid question test
	request. Passes important attributes of our TestCase to
	the test_case_factory for our desired TestCase.

	Args:
		module: module containing functions to be tested
		question: user's requested question test (string)
		question_inputs: all question function test inputs
			and expected results

	Returns:
		the desired TestCase for this question
	"""
	# ensures that question is formated as
	# 'q#' with # > 0
	try:
		assert match(r'q[1-9][0-9]*', question)
		assert question in question_inputs
	except:
		print("That is not a question in the file being tested.")
		print("Make sure you're inputting your question in the")
		print("specified form as per the README.md file.")
		return

	# Defines the q#Test class with all the function tests dynamically
	# added to the definition of the class

	return test_case_factory(question + 'Test', module, question_inputs[question])

def test_case_factory(name, module, func_inputs):
	"""
	Produces a subclass of unittest.TestCase with test
	functions for all the functions we want to test from
	module specified in func_inputs (i.e. all functions
	in this specified question) dynamically added.

	Args:
		name: name of the class; format: q#Test
		module: module which contains the functions to be tested
		func_inputs: all test inputs for each function to be
			tested and the expeceted outputs for each test input

	Returns:
		a subclass of unittest.TestCase
	"""
	dic = {}
	for func in func_inputs:
		dic["test_" + func] = test_compose(module, func, func_inputs[func])
	newclass = type(name, (unittest.TestCase,), dic)
	return newclass

def test_compose(module, func, inputs):
	"""
	Produces a test function to be added to a
	unittest.TestCase class which will call test
	on the desired function found by name and the
	inputs provided.
	
	Args:
		module: module that contains func
		func: name of function to be tested
		inputs: arguments to be tested in the
			provided function and their expected
			results
	
	Returns:
		a function to be dynamically added to the
		TestCase clas as a test function for a
		specific function in the specified module
	"""
	def test_run(self):
		test(getattr(module, func), inputs)
	return test_run

def test(func, inputs):
	"""
	Calculates the received outputs for all tests of the
	designated function and forms a list of received
	outputs, expected outputs, and args passed into the
	function. Passes this into run_tests for testing
	equality among received vs. expected outputs and
	display of results of tests.

	Args:
		func: function being tested
		inputs: list with each item containing args to be
			passed into function and the expected output
			from each function call with those args
	"""
	tests = list(map(lambda inp: (func(*inp[0]), inp[1], inp[0]), inputs))
	run_tests(func.__name__, tests)

def run_tests(test_name, tests):
	"""
	Goes through the received outputs and expected outputs
	of the function being tested and asserts if they are
	equal. Prints if a received output differs from the
	expected output. Prints how many tests were passed for
	this function.

	Args:
		test_name: name of the function being tested; used
			for printing purposes
		tests: list of tuples containing received output,
			expected output, and args passed into the
			function; each list item represents one test
			of the function
	"""
	tests_passed = 0
	print(test_name, "tests:")
	for test in tests:
		try:
			assert test[0] == test[1]
			tests_passed += 1
		except:
			print("    Arguments:", test[2], "Expected:", test[1], " Received:", test[0])
			break
	print("   ", tests_passed, "out of", len(tests), "passed")
	print()

class q(unittest.TestCase):
	"""
	DO NOT DELETE THIS CLASS
	"""
	pass
