import unittest, sys
from graderlib import test_case
import practice as module

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
		], "square": [
			[(2,), 4],
			[(3,), 9],
			[(10,), 100]
		]
	},
	"q2": {
		"quart": [
			[(2,), 16],
			[(3,), 81],
			[(4,), 256]
		],
		"cube": [
			[(2,), 8],
			[(5,), 125],
			[(19,), 6859]
		]
	},
	"q3": {
		"merge_strings": [
			[("a", "b"), "ab"],
			[("cat", "dog"), "catdog"],
			[("meat", "ball"), "meatball"],
			[([1, 40, 3], [2, 4, 6]), [1, 40, 3, 2, 4, 6]]
		],
		"stringed_out": [
			[("abcde",), ['a', 'c', 'e']],
			[("aabbcc",), ['a', 'b', 'c']],
			[("1ab23c",), ['1', 'b', '3']],
			[([0, 1, 2, 3, 4],), [0, 2, 4]]
		],
		"length_of_str": [
			[('abcdefghijkl',), 12],
			[('code it!',), 8],
			[([3, 1, 2, 0],), 4]
		],
		"slice1": [
			[('yeah yeah yeah', 10), 'yeah'],
			[('The Beatles', 4), 'Beatles'],
			[('lampost', 3), 'post'],
			[(['1', 2, '3', 4, '5', 6], 3), [4, '5', 6]]
		],
		"slice2": [
			[('heyo', 3), 'hey'],
			[('suppppppp', 5), 'suppp'],
			[('worst trade deal ever', 2), 'wo'],
			[(['hi', 'hello', 'howdy', 'cheerio'], 3), ['hi', 'hello', 'howdy']]
		],
		"slice_and_dice": [
			[('abc123zyx987', 4, 8), '23zy'],
			[('racecar', 1, 6), 'aceca'],
			[("(^::'^(", 0, 3), '(^:'],
			[([1, 2, 3, 4, 5], 3, 4), [4]]
		],
		"chop_it_up": [
			[('Rolltide', 'iiiiinnn'), 'Rollinnn'],
			[('yummy', 'tummy'), 'yummy'],
			[('Joe Biden ', 'Obama'), 'Joe Bama'],
			[([1, 2, 3, 4], [6, 7, 9, 8]), [1, 2, 9, 8]]
		]
	},
	"q4": {
		"powerful_func": [
			[([1, 2, 3, -1, 4, 2],), 1],
			[([4, 2, 1, 0.5, 0.25, 0.125],), 0.0625],
			[([3, 5, 7, 1, 3, 5],), 9]
		],
		"stretch_func": [
			[
				([1, 2, 3],),
				[1, 2, 1, 3, 2, 3]
			],
			[
				(["a", "b", "c", "d"],),
				["a", "b", "d", "a", "c", "d", "b", "c", "d"]
			],
			[
				([0, 1, 2, 3, 4],),
				[0, 1, 3, 4, 0, 2, 3, 4, 1, 2, 3, 4]
			]
		],
		"quart_and_square": [
			[([0, 3, 2, 1],), ('RESULT', 45)],
			[([-1, -4, -8, -9, -7],), ('RESULT', -840)],
			[([-1, 1, -2, 2, -3, 3],), ('RESULT', 81)]
		]
	},
	"q5": {
		"wardrobe": [
			[
				({}, ["Puma", "Reebok", "Vans"], [5, 15, 25]),
				{
					"jackets": {"Ralph Polo": 40},
					"shoes": {"Puma": 5, "Reebok": 15, "Vans": 25}
				}
			],
			[
				({"Lacoste": 50}, ["Puma", "Reebok", "Vans"], [5, 15, 25]),
				{
					"jackets": {"Lacoste": 50, "Ralph Polo": 40},
					"shoes": {"Puma": 5, "Reebok": 15, "Vans": 25}
				}
			]
		]
	}
}

def run_test(questions):
	for question in questions:
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

	# Displays which questions are being tested
	plural = ('s ' if len(questions) > 1 else ' ')
	q_string = ', '.join([questions[i][1:] for i in range(len(questions))])
	print('\nRunning Test' + plural + 'for Question' + plural + q_string)
	print()


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
	do so), so leave argv='q'.
	"""
	unittest.main(argv='q')

def main():
	# Test all questions.
	if len(sys.argv) == 1:
		run_test([question for question in question_inputs])
	# Test one specific question specified
	# by the single argument passed in.
	elif len(sys.argv) == 2:
		run_test([sys.argv[1]])
	# Too many arguments.
	else:
		run_test([sys.argv[i] for i in range(1, len(sys.argv))])

if __name__ == '__main__':
	main()
