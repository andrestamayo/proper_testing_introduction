from copy import copy

class Matrix(object):
	def __init__(self, *args):
		#Task1
		self.rows=[]		
		for elem in args:		
			self.rows.append(elem)
		e=0
		i=0
		i=len(self.rows)
		e=len(args[0])
		self.shape=(i,e)
		
		pass


	def indices_generator(self):
		#Task2
		list_indices = []
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				list_indices.append((i,j))
		return list_indices
		pass

	def apply(self, fun, **kwargs):
		#Task3
		# must use indices_generator (task2)
		for elem in self.indices_generator():
        		self.rows[elem[0]][elem[1]]=fun(self.rows[elem[0]][elem[1]])
	
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

if __name__ == '__main__':
	m1 = Matrix([1,2,1],[3,3,3],[5,5,5])
	print(m1)	


"""
The output of those lines:

m1 = Matrix([1,2,1],[3,3,3],[5,5,5])
m2 = Matrix([[1,1,3],[1,1,3],[0,0,3]])
print m1
print m2
m3= m1+m2
print m3
print m2
<<<<<<< HEAD
print m1+3
=======
print m1+3  
>>>>>>> b_3
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
