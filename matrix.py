from copy import copy

class Matrix(object):
	def __init__(self, *args):
		#Task1

		if(len(arg)!=1):
			self.rows= args
			e=0
			i=0
			i=len(self.rows)
			e=len(args[0])
			self.shape=(i,e)
		else:
			self.rows= args[0]
			e=0
			i=0
			i=len(self.rows)
			e=len(args[0][0])
			self.shape=(i,e)	


	def indices_generator(self):
		#Task2
		pass

	def apply(self, fun, **kwargs):
		#Task3
		# must use inidices_generator (task2)
		pass

	def __add__(self, m):
		#Task4
		# must use apply (task3)
		pass

	@property
	def transpose(self):
		#Task5
		# transpose the matrix
		pass

	def __str__(self):
		#Task6
		# return the string representation
		pass

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
