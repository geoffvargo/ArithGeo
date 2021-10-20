## https://coderbyte.com/results/gvargo:Arith%20Geo:Python3 ##
from termcolor import colored
import math


def ArithGeo(arr):
	# code goes here
	# print(f'arr is of {type(arr)}')
	
	is_arith = True
	is_geom = True
	
	count = arr.__len__()
	# curr_d = -1
	# curr_r = -1
	
	diffs = []
	ratios = []
	
	for i in range(1, count):
		curr_d = arr[i] - arr[i - 1]
		curr_r = arr[i] / arr[i - 1]
		if diffs.__len__() > 0 and curr_d != diffs[-1]:
			is_arith = False
		if ratios.__len__() > 0 and curr_r != ratios[-1]:
			is_geom = False
		diffs.append(curr_d)
		ratios.append(curr_r)
	
	# print(f'diffs = {diffs}')
	# print(f'ratios = {ratios}')
	
	if is_geom:
		return 'Geometric'
	elif is_arith:
		return 'Arithmetic'
	else:
		return '-1'


if __name__ == '__main__':
	# keep this function call here
	s = [int(x) for x in input().rstrip()[1:-1].split(sep=',')]
	print(colored(s, color='green'))
	print(ArithGeo(s))
