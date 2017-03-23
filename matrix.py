from copy import copy

class Matrix(object):
	def __init__(self, *args):
		#Task1

	def indices_generator(self):
		#Task2


	def apply(self, fun, **kwargs):
		#Task3
		# must use inidices_generator (task2)

	def __add__(self, m):
		#Task4
		# must use apply (task3)
	"""mat1= [[1,2],[3,4],[5,6],[7,8]]
	mat2=[[9,10],[11,12],[13,14],[15,16]]

	def __add__(self, m):
		res = []
		for rrow in self:
			print res
			res[rrow]=self[rrow]
			for ccol in self[rrow]:
				res[rrow][ccol]=self[rrow][ccol]
				res[rrow][ccol]=self[rrow][ccol]+m[rrow][ccol]
		print res
		return res


	print (mat1).__add__(mat2)
	"""

	@property
	def transpose(self):
		#Task5
		# transpose the matrix

	def __str__(self):
		#Task6
		# return the string representation

"""
The output of those lines:

m1 = Matrix([1,2,1],[3,3,3],[5,5,5])
m2 = Matrix([[1,1,3],[1,1,3],[0,0,3]])
print m1
print m2
m3= m1+m2
print m3
print m2
print m1+3  
print m1.transpose

Should be following:

|1 2 1|
|3 3 3|
|5 5 5|

|1 1 3|
|1 1 3|
|0 0 3|

|2 3 4|
|4 4 6|
|5 5 8|

|1 1 3|
|1 1 3|
|0 0 3|

|4 5 4|
|6 6 6|
|8 8 8|

|1 3 5|
|2 3 5|
|1 3 5|



"""
