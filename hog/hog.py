"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
	"""Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
	the outcomes unless any of the outcomes is 1. In that case, return 0.
	"""
	# These assert statements ensure that num_rolls is a positive integer.
	assert type(num_rolls) == int, 'num_rolls must be an integer.'
	assert num_rolls > 0, 'Must roll at least once.'
	# BEGIN Question 1
	points = 0
	for i in range(num_rolls):
		roll = dice()
		if roll == 1:
			for n in range(i+1,num_rolls):
				dice()
			return 0
		else: 
			points += roll
	return points
	# END Question 1

def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				return False
		return True
	else:
		return False

def nextprime(n):
	guess = n+1
	while not isprime(guess):
		guess += 1
	return guess

def take_turn(num_rolls, opponent_score, dice=six_sided):
	"""Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

	num_rolls:       The number of dice rolls that will be made.
	opponent_score:  The total score of the opponent.
	dice:            A function of no args that returns an integer outcome.
	"""
	assert type(num_rolls) == int, 'num_rolls must be an integer.'
	assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
	assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
	assert opponent_score < 100, 'The game should be over.'
	# BEGIN Question 2
	if num_rolls == 0:
		max = 0
		for i in str(opponent_score):
			n = int(i)
			if n > max:
				max = n
		points = max + 1
	else:
		points = roll_dice(num_rolls,dice)
	if isprime(points):
		points = nextprime(points)
	return points

	# END Question 2


def select_dice(score, opponent_score):
	"""Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
	multiple of 7, in which case select four-sided dice (Hog wild).
	"""
	# BEGIN Question 3
	if (score + opponent_score) % 7 == 0:
		return four_sided
	else:
		return six_sided
	# END Question 3


def is_swap(score0, score1):
	"""Returns whether the last two digits of SCORE0 and SCORE1 are reversed
	versions of each other, such as 19 and 91.
	"""
	# BEGIN Question 4
	sscore0 = str(score0)
	sscore0 = sscore0[-2:]
	sscore1 = str(score1)
	sscore1 = sscore1[-2:]

	if len(sscore0) == 1:
		sscore0 = '0' + sscore0

	if len(sscore1) == 1:
		sscore1 = '0' + sscore1

	if sscore1[::-1] == sscore0:
		return True
	else:
		return False
	# END Question 4


def other(who):
	"""Return the other player, for a player WHO numbered 0 or 1.

	>>> other(0)
	1
	>>> other(1)
	0
	"""
	return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
	"""Simulate a game and return the final scores of both players, with
	Player 0's score first, and Player 1's score second.

	A strategy is a function that takes two total scores as arguments
	(the current player's score, and the opponent's score), and returns a
	number of dice that the current player will roll this turn.

	strategy0:  The strategy function for Player 0, who plays first
	strategy1:  The strategy function for Player 1, who plays second
	score0   :  The starting score for Player 0
	score1   :  The starting score for Player 1
	"""
	who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
	# BEGIN Question 5
	while score0 < goal and score1 < goal:
		dice = select_dice(score0,score1)
		if who == 0:
			num_rolls = strategy0(score0,score1)
			points = take_turn(num_rolls,score1,dice)
			score0 += points
			if points == 0:
				score1 += num_rolls
		if who == 1:
			num_rolls = strategy1(score1,score0)
			points = take_turn(num_rolls,score0,dice)
			score1 += points
			if points == 0:
				score0 += num_rolls
		if is_swap(score0,score1) == True:
			score0,score1 = score1,score0
		who = other(who)
	# END Question 5
	return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
	"""Return a strategy that always rolls N dice.

	A strategy is a function that takes two total scores as arguments
	(the current player's score, and the opponent's score), and returns a
	number of dice that the current player will roll this turn.

	>>> strategy = always_roll(5)
	>>> strategy(0, 0)
	5
	>>> strategy(99, 99)
	5
	"""
	def strategy(score, opponent_score):
		return n

	return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
	"""Return a function that returns the average_value of FN when called.

	To implement this function, you will have to use *args syntax, a new Python
	feature introduced in this project.  See the project description.

	>>> dice = make_test_dice(3, 1, 5, 6)
	>>> averaged_dice = make_averaged(dice, 1000)
	>>> averaged_dice()
	3.75
	>>> make_averaged(roll_dice, 1000)(2, dice)
	5.5

	In this last example, two different turn scenarios are averaged.
	- In the first, the player rolls a 3 then a 1, receiving a score of 0.
	- In the other, the player rolls a 5 and 6, scoring 11.
	Thus, the average value is 5.5.
	Note that the last example uses roll_dice so the hogtimus prime rule does
	not apply.
	"""
	# BEGIN Question 6
	def avg(*args):
		total = 0
		for i in range(num_samples):
			total += fn(*args)
		ave = total / num_samples
		return ave
	return avg

	# END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
	"""Return the number of dice (1 to 10) that gives the highest average turn
	score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
	Assume that dice always return positive outcomes.

	>>> dice = make_test_dice(3)
	>>> max_scoring_num_rolls(dice)
	10
	"""
	# BEGIN Question 7
	max = 0
	num = 1
	for i in range(1,11):
		avpoints = make_averaged(roll_dice,num_samples)(i,dice)
		if avpoints > max:
			max = avpoints
			num = i
	return num
	# END Question 7


def winner(strategy0, strategy1):
	"""Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
	score0, score1 = play(strategy0, strategy1)
	if score0 > score1:
		return 0
	else:
		return 1


def average_win_rate(strategy, baseline=always_roll(5)):
	"""Return the average win rate of STRATEGY against BASELINE. Averages the
	winrate when starting the game as player 0 and as player 1.
	"""
	win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
	win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

	return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
	"""Run a series of strategy experiments and report results."""
	if False:  # Change to False when done finding max_scoring_num_rolls
		six_sided_max = max_scoring_num_rolls(six_sided)
		print('Max scoring num rolls for six-sided dice:', six_sided_max)
		four_sided_max = max_scoring_num_rolls(four_sided)
		print('Max scoring num rolls for four-sided dice:', four_sided_max)

	if True:  # Change to True to test always_roll(8)
		print('always_roll(8) win rate:', average_win_rate(always_roll(5)))

	if False:  # Change to True to test bacon_strategy
		print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

	if False:  # Change to True to test swap_strategy
		print('swap_strategy win rate:', average_win_rate(swap_strategy))

	"*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
	"""This strategy rolls 0 dice if that gives at least MARGIN points,
	and rolls NUM_ROLLS otherwise.
	"""
	if take_turn(0, opponent_score) >= margin:
		return 0
	else:
		return num_rolls
	# END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
	"""This strategy rolls 0 dice when it results in a beneficial swap and
	rolls NUM_ROLLS otherwise.
	"""
	# BEGIN Question 9
	pscore = score + take_turn(0, opponent_score)
	if is_swap(pscore,opponent_score) == True and pscore < opponent_score:
		return 0
	else:
		return num_rolls
	# END Question 9

def final_strategy(score, opponent_score):
	"""Write a brief description of your final strategy.

	My strategy first calculates the potential turn score if 0 dice are rolled and we account
	for free bacon and hogtimus prime. Using that value I determine whether or not it would be
	detrimental to swap with the opponents score at the end of the turn. Next there are several
	conditions where I would roll 0:
	- Free bacon gives more points than the average of the dice being rolled.
	- Swap strategy is beneficial
	- The opponent can be forced to roll four sided dice
	If none of these conditions are met the number of die that gives the highest average score
	based on what kind of dice are being rolled is returned.
	"""
	# BEGIN Question 10
	pscore = take_turn(0,opponent_score) + score
	if is_swap(pscore,opponent_score) == True and pscore >= opponent_score:
		safeswap = False
	else:
		safeswap = True
	if select_dice(score,opponent_score) == four_sided:
		if (bacon_strategy(score,opponent_score,4,3) == 0 or swap_strategy(score,opponent_score,3) == 0 or pscore > 100 or select_dice(opponent_score,pscore) == four_sided) and safeswap == True:
			num_rolls = 0
		else:
			num_rolls = 3
	elif select_dice(score,opponent_score) == six_sided:
		if (bacon_strategy(score,opponent_score,6,6) == 0 or swap_strategy(score,opponent_score,6) == 0 or pscore > 100 or select_dice(opponent_score,pscore) == four_sided) and safeswap == True:
			num_rolls = 0
		else:
			num_rolls = 6
	return num_rolls# Replace this statement
	# END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
	"""Read in the command-line argument and calls corresponding functions.

	This function uses Python syntax/techniques not yet covered in this course.
	"""
	import argparse
	parser = argparse.ArgumentParser(description="Play Hog")
	parser.add_argument('--run_experiments', '-r', action='store_true',
						help='Runs strategy experiments')

	args = parser.parse_args()

	if args.run_experiments:
		run_experiments()
