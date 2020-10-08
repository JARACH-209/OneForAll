from typing import Callable, List
import math
#DO NOT MAKE UNNECESSARY CHANGES
class DistanceFuncs:
	def calc_distance(self, point_a: List[float], point_b: List[float], dist_func: Callable)->float:
	""" Calculates distance between two points using the passed dist_func """
		return dist_func(point_a, point_b)
	@staticmethod
	def euclidean(point_a: List[float], point_b: List[float],/)->float:
"""
Calculates Euclidean Distance between two points Example:
>>> DistanceFuncs.euclidean([1,1],[1,1])
0.0
"""
		return math.dist(point_a, point_b)
	@staticmethod
	def manhattan_distance(point_a: List[float], point_b: List[float]): """Compute
	the manhattan_distance between two points""" 
		raise NotImplementedError()
	@staticmethod
	def jaccard_distance(point_a: List[float], point_b: List[float]): """Compute
the jaccard_distance between two points""" 
		raise NotImplementedError()
defmain():
"""Demonstrate the usage of DistanceFuncs """
	test = DistanceFuncs()
	test.calc_distance([2,3],[10,10])
	print("The distance is : ",test.euclidean())
if name ==" main ":
main()