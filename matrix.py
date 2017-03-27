class Matrix(object):

    '''Dear teammates,
            I used a different perpective and tried to programma everything from scrach.
            Just try to take a look.
            I am exausted. I will explain everything if you ask me.
            We have to call the function fun as argument for apply inside __add__
            '''

    def __init__(self, *args):
        #Task1
        if len(args) == 1:  # if the argument is 1 list of lists
            args = args[0]  # replace with the values of this list as new arguments
        self.rows = []
        for i in range(len(args)):  # for every argument
            self.rows.append(args[i])  # add this to the matrix.rows[] one by one
        self.shape = (len(args),len(args[0]))
        pass

    def indices_generator(self):
        """ Generate the index list of each coefficient
        Input:
        Output:
            list_indices = list of indexes
        """
        # Task2
        list_indices = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                list_indices.append((i, j))
        return list_indices
        pass

    def apply(self, fun, **kwargs):
        # comments
        indexed_list = self.indices_generator() #create a list with indeces
        resmat = []
        for each in indexed_list:  # create a new matrix as result
            resmat[indexed_list[each]] = fun(self.rows[indexed_list[each]],kwargs.rows[indexed_list[each]])  # use fun
        return resmat
        pass


    def __add__(self, m):
        def prosthese(theother):###### i am so close. just have to know how to pass the arguments correctly
            return self+theother
        return self.apply(prosthese(m),m)
        pass

    @property
    def transpose(self):
        """ Transpose a matrix
        Input:
        Output:
            transposed matrix
        """
        # Task5
        # transpose the matrix
        new_rows = []  # list with new coefficients
        for i in range(self.shape[1]):  # initialisation of the size of matrix
            new_rows.append([0] * self.shape[0])
        for tuples in self.indices_generator():
            new_rows[tuples[1]][tuples[0]] = self.rows[tuples[0]][tuples[1]]
        return Matrix(new_rows)  # creation of a new matrix with the good coefficients
        pass

    def __str__(self):
        """ Return string representation of a matrix
        """
        # Task6
        # return the string representation
        i = 0  # row index
        m_string = '|'
        for tuples in self.indices_generator():
            if tuples[0] == i:
                m_string += str(self.rows[tuples[0]][tuples[1]]) + " "
            else:
                m_string = m_string[:-1]
                m_string += "|\n|" + str(self.rows[tuples[0]][tuples[1]]) + " "
                i += 1
        m_string = m_string[:-1]
        m_string += '|\n'
        return m_string
        pass

# restored as it was. please do not change original instructions.
m1 = Matrix([1,2,1],[3,3,3],[5,5,5])
m2 = Matrix([[1,1,3],[1,1,3],[0,0,3]])
print m1
print m2
m3= m1+m2
print m3
print m2
print m1+3
print m1.transpose

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
