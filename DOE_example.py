from DOE import *

###	NOTE YOU WILL NEED TO TAKE CARE OF RANDOMIZING THAT IS CURRENTLY NOT SUPPORTED

def convert_doe_to_levels(doe, factor_levels):
	Converting the 0's and 1's to actual factor levels
	number_of_factors = len(factor_levels)
	converted_doe = numpy.zeros_like(doe)
	
	for factor_id in range(number_of_factors):
		levels = factor_levels[factor_id]
		
		for level in range(len(levels)):
			level_locs = (doe[:, factor_id] == level)
			converted_doe[:, factor_id][level_locs] = levels[level]
	
	return converted_doe
	
#Setting up a 2 level factorial experiment
number_of_factors = 3
two_level_factorial_levels = [
	[0.0, 1.0],
	[100.0, 600.0],
	[1, 5]
	]
two_level_factorial = Factorial().full_2_level(number_of_factors)
print('Two level factorial DOE')
print(two_level_factorial)

converted_two_level_factorial = convert_doe_to_levels(two_level_factorial, two_level_factorial_levels)
print('Two level factorial DOE converted to the real experimental values')
print(converted_two_level_factorial)


#setting up a multilevel factorial experiment
full_factorial_levels = [
	[0.5, 1.0, 2.5],
	[500.0, 100.0, 60., 80.],
	[5.0, 100.0],
	]
factor_levels = [3, 4, 2]
full_factorial_exp = Factorial().full(factor_levels, reps=2)
print('Full factorial experiment')
print(full_factorial_exp)
converted_full_factorial_exp = convert_doe_to_levels(full_factorial_exp, full_factorial_levels)
print('Full factorial experiment converted to real experimental values')
print(converted_full_factorial_exp)

setting up a central composite experiment
cc_factors = 5
cc_levels = [
	[5, 10, 15],
	[4, 9, 14],
	[3, 8, 13],
	[2, 7, 12],
	[1, 6, 11],
	]
cc_doe = CentralComposite().doe(cc_factors, center_points='d', alpha_type='faced')
print('Central Composite design of experiment')
print(cc_doe)
converted_cc_doe = convert_doe_to_levels(cc_doe, cc_levels)
print('Central Composite design of experiment converted to real experimental values')
print(converted_cc_doe)
