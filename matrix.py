from copy import copy

class Matrix(object):
	def __init__(self, *args):
		""" Constructor for a matrix
		Input:
			a list of lists of coefficients for each row / lists of coefficients for each row
		Output:
			.rows = coefficients of the matrix
			.shape = dimension of the matrix

		A vector (1xN matrix) has to be init with [[...]]
		"""
		#Task1
		if(len(args)!=1):
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
		pass

	def indices_generator(self):
		""" Generate the index list of each coefficient
		Input:
		Output:
			list_indices = list of indexes
		"""
		#Task2
		list_indices = []
		for i in range(self.shape[0]):
			for j in range(self.shape[1]):
				list_indices.append((i,j))
		return list_indices
		pass

	def apply(self, fun, **kwargs):
		""" Apply a function to every coefficients or specific coefficients
		Input:
			fun = function to apply
			**kwargs = specific coefficients to change 
		Output:
			
		
		There is the case if kwargs is specified and correspond to specific coefficients		
		"""
		#Task3
		# must use indices_generator (task2)
		if len(kwargs) == 0:
			for elem in self.indices_generator():
        			self.rows[elem[0]][elem[1]]=fun(self.rows[elem[0]][elem[1]])			
		pass
	
	def __add__(self, m):
		""" Define the operation + for matrix
		Input:
			m = second member of the operation. It can be another matrix or a scalar
		Output:
			result of operation
		
		Try to find how to use apply
		Raise an error if the type is not correct
		"""
		#Task4
		# must use apply (task3)
		if type(self)==type(m):	#if sum of two matrices	
			new_rows = [] #list with new coefficients
			for i in range(self.shape[0]):#initialisation of the size of matrix
				new_rows.append([0]*self.shape[1])
			for tuples in self.indices_generator() :
				new_rows[tuples[0]][tuples[1]]=self.rows[tuples[0]][tuples[1]]+m.rows[tuples[0]][tuples[1]]
			return Matrix(new_rows)#creation of a new matrix with the good coefficients
		else: #if one matrix + one scalar
			new_rows = [] #list with new coefficients
			for i in range(self.shape[0]):#initialisation of the size of matrix
				new_rows.append([0]*self.shape[1])
			for tuples in self.indices_generator() :
				new_rows[tuples[0]][tuples[1]]=self.rows[tuples[0]][tuples[1]]+m
			return Matrix(new_rows)#creation of a new matrix with the good coefficients
        	pass

	@property
	def transpose(self):
		""" Transpose a matrix
		Input:
		Output:
			transposed matrix
		"""
		#Task5
		# transpose the matrix
		new_rows = [] #list with new coefficients
		for i in range(self.shape[1]): #initialisation of the size of matrix
			new_rows.append([0]*self.shape[0])
		for tuples in self.indices_generator() :
			new_rows[tuples[1]][tuples[0]]=self.rows[tuples[0]][tuples[1]]
		return Matrix(new_rows) #creation of a new matrix with the good coefficients
		pass

	def __str__(self):
		""" Return string representation of a matrix
		"""
		#Task6
		# return the string representation
		i=0 #row index
		m_string ='|'
		for tuples in self.indices_generator() :
			if tuples[0]==i:
				m_string+=str(self.rows[tuples[0]][tuples[1]])+" "
			else:
				m_string=m_string[:-1]				
				m_string+="|\n|"+str(self.rows[tuples[0]][tuples[1]])+" "
				i+=1
		m_string=m_string[:-1]		
		m_string+='|\n'
		return m_string
		pass


if __name__ == '__main__':
	m1 = Matrix([1,2,1],[3,3,3],[5,5,5])
	m2 = Matrix([[1,1,3],[1,1,3],[0,0,3]])
	m4 = Matrix([[3, 3, 3]])
	m5 = Matrix([2],[2],[2])
	print m1
	print m2
	print m4
	print m5
	m3= m1+m2
	print m3
	print m2
	print m1+3
	print m1.transpose
	print m4.transpose
	print m5.transpose


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
