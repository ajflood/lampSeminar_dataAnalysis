import numpy
import math
import logging

logger = logging.getLogger('doe')

logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(name)s:%(levelname)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Factorial:
	'''Class used to design various factorial experiment'''

	def full(self, factor_levels, reps=1):
		num_factors = len(factor_levels)
		logger.debug('Creating a full factorial experiment with %i factors' %num_factors)
		num_runs = numpy.product(factor_levels)
		logger.debug('Need to perform %i experimental runs for factorial experiment' %(num_runs * reps))
		
		experiment = numpy.zeros((num_runs, num_factors))
		available_space = num_runs
		for factor in range(num_factors):
			num_levels = factor_levels[factor]
			level_reps = int(available_space / num_levels)
			factor_experiment = numpy.empty(0)
			for level in range(num_levels):
				factor_experiment = numpy.concatenate((factor_experiment, numpy.full(level_reps, level)))
			
			factor_experiment = numpy.tile(factor_experiment, int(num_runs/available_space))
			experiment[:, factor] = factor_experiment
			available_space = level_reps
		
		return numpy.repeat(experiment, reps, axis=0)
		
	def full_2_level(self, num_factors):
		'''Generates a 2 level factorial for a given number of factors'''
		logger.debug('Creating a 2 level full factorial experiment for %i factors' %num_factors)
		factor_level = 2 * numpy.ones((num_factors), dtype=int)
		return self.full(factor_level)

class CentralComposite:
	'''Class for designing central composite design experiments'''
	
	def doe(self, num_factors, center_points='d', alpha_type='faced'):
		'''Generates a design of experiment for CCD experiment'''
		edges = Factorial().full_2_level(num_factors)
		edges[edges==0] = -1
		
		star = numpy.zeros((2**num_factors, num_factors))
		for i in range(num_factors):
			star[2*i:2*i+2, i] = [-1, 1]
		if alpha_type == "faced":
			alpha = 1
		elif alpha_type == "orthogonal":
			#alpha = (2**n)**0.25
			alpha = math.sqrt(2**(num_factors*0.5))
		star *= alpha
		
		if center_points == 'd':
			center_points = num_factors
		center = numpy.zeros((center_points, num_factors))	
			
		experiment = numpy.vstack((edges, star, center))
		logger.debug("CC Design requires %i experiments" %numpy.shape(experiment)[0])
		return experiment + 1

class Plackett_Burman:
	'''Creates a Plackett-Burman design of experiment'''
	def __init__(self):
		self.generator_8 = '+++-+--'
		self.generator_12 = '++-+++---+-'
		self.generator_16 = '++++-+-++--+---'
		self.generator_20 = '++--++++-+-+----++-'
		self.generator_24 = '+++++-+-++--++--+-+----'
		self.generator_36 = '-+-+++---+++++-+++--+----+-+-++--+-'
	
	def sign_converter(self, sign):
		if sign == '+':
			return 1.0
		elif sign == '-':
			return -1.0
		else:
			return 1000.0
		
	def doe(self, num_factors):
		if num_factors < 8:
			generator = self.generator_8
			num_runs = 8
		elif 8 <= num_factors < 12:
			generator = self.generator_12
			num_runs = 12
		elif 12 <= num_factors < 16:
			generator = self.generator_16
			num_runs = 16
		elif 16 <= num_factors < 20:
			generator = self.generator_20
			num_runs = 20
		elif 20 <= num_factors < 24:
			generator = self.generator_24
			num_runs = 24
		elif 24 <= num_factors < 36:
			generator = self.generator_36
			num_runs = 36
		else:
			print('Generator not found')
		
		experiment = numpy.zeros((num_runs, num_factors))
		seed = numpy.array([self.sign_converter(char) for char in list(generator)])
		
		for factor in range(num_factors):
			experiment[0:len(seed), factor] = seed
			seed = numpy.roll(seed,1)
		experiment[experiment==0.] = -1.
		
		return experiment
