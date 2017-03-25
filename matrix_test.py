import unittest
from matrix import Matrix

class MyTest1(unittest.TestCase):

	def setUp(self):
		self.l1 = [[1,2,1],[3,3,3],[5,5,5]]
		self.l2 = [[1,1,3],[1,1,3]]
		self.l3 = [[3, 3, 3]]

	def test_init(self):
		m1 = Matrix(*self.l1) #add * 
		m2 = Matrix(*self.l2)	
		m3 = Matrix(*self.l3)
		self.assertEqual(self.l1[0],m1.rows[0])
		self.assertEqual(self.l1[1],m1.rows[1])
		self.assertEqual(self.l1[2],m1.rows[2])

		self.assertEqual(self.l2[0],m2.rows[0])
		self.assertEqual(self.l2[1],m2.rows[1])

		self.assertEqual(self.l3,m3.rows)

		self.assertEqual((3,3), m1.shape)
		self.assertEqual((2,3), m2.shape)
		self.assertEqual((1,3),m3.shape)


class MyTest2(unittest.TestCase):

	def setUp(self):
		self.l1 = [[1,2],[3,3]]
		self.l2 = [[1,3],[1,1]]
		self.m1 = Matrix(*self.l1) #add *
		self.m2 = Matrix(*self.l2)
		self.m3 = Matrix([1,2],[3,4])
		self.m5 = Matrix([1,2,4],[0,0,0])

	def test_indices_generator(self):
		gen = list(self.m3.indices_generator())
		gen_exp = [(0,0),(0,1),(1,0),(1,1)]
		self.assertListEqual(gen, gen_exp)

	def test_apply(self):
		def divide_by_four(x):
			return x/4.0
		self.m3.apply(divide_by_four)
		self.assertEqual(self.m3.rows[0][0],0.25)
		self.assertEqual(self.m3.rows[0][1],0.50)
		self.assertEqual(self.m3.rows[1][0],0.75)
		self.assertEqual(self.m3.rows[1][1],1.0)

	def test_add(self):
		m4 = self.m1+2
		m5 = self.m1+self.m2
		self.assertEqual(m4.rows[0][0],3)
		self.assertEqual(m4.rows[0][1],4)
		self.assertEqual(m4.rows[1][0],5)
		self.assertEqual(m4.rows[1][1],5)

		self.assertEqual(m5.rows[0][0],2)
		self.assertEqual(m5.rows[0][1],5)
		self.assertEqual(m5.rows[1][0],4)
		self.assertEqual(m5.rows[1][1],4)
		
	
	def test_transpose(self):
		m = self.m3.transpose
		self.assertEqual(m.rows[0][0],1)
		self.assertEqual(m.rows[0][1],3)
		self.assertEqual(m.rows[1][0],2)
		self.assertEqual(m.rows[1][1],4)

	def test_string(self):
		str_m = str(self.m5)
		self.assertEqual(str_m,"|1 2 4|\n|0 0 0|\n")

if __name__ == '__main__':
	unittest.main()

