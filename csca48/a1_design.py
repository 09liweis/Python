class Matrix(Objective):
    '''A class represents a mathmatical matrix'''

    def __init__(self, num_row, num_cow):
        '''(Matrix, int, int) -> None
        This is to initialing the dimension of the matrix
        '''
        pass

    def get_row(self, row_num):
        '''(Matrix, int) -> list
        This function return the nth row of given number.
        If this row doesn't exist, it will raise an RowNotExist error
        '''
        pass

    def set_row(self, lists):
        '''(Matrix, list of list) -> None
        This function set the value of rows of the matrix
        after initializing a new object.
        '''
        pass

    def get_col(self, col_num):
        '''(Matrix, int) -> list
        This function return the nth column of given number.
        If this row doesn't exist, it will raise an ColNotExist error
        '''
        pass

    def set_col(self, lists):
        '''(Matrix, list of list) -> None
        This function set the value of col of matrix
        after initializing a new object.
        '''
        pass

    def multiply(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        This function is doing an multiply operation based on linear algebra
        fundamental. If matirces' dimensions don't match, it will raise a
        MatrixNotMatch error.
        '''
        pass

    def add(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        This function is doing an adding operation based on linear algebra
        fundamental. If matirces' dimensions don't match, it will raise a
        MatrixNotMatch error.
        '''
        pass

    def subtract(self, matrix):
        '''(Matrix, Matrix) -> Matrix
        This function is doing an subtracting operation based on linear algebra
        fundamental. If matirces' dimensions don't match, it will raise a
        MatrixNotMatch error.
        '''
        pass

    def transpose(self):
        '''(Matrix) -> None
        This function mutates the list in order to change matrix into
        transposed form.
        '''
        pass

    def swap_row(self, first, second):
        '''(Matrix, int, int) -> None
        This function mutate the list by interchanging tow rows.
        '''
        pass

    def swap_col(self, first, second):
        '''(Matrix, int, int) -> None
        This function mutate the list by interchanging tow columns.
        '''
        pass

    def swap_row_n_col(self, row_num, col_num):
        '''(Matrix, int, int) -> None
        This function mutate the list by interchanging a row with a colunm in
        a nxn matrix. Otherwise, it will raise MatrixNotMatch error.
        '''
        pass

    def get_matrix(self):
        '''(Matrix) -> list of obj
        This function return the whole matrix
        '''
        pass

    def set_matrix(self, matrix):
        '''(Matrix, list of obj) -> None
        This function set the matrix
        '''


class Square_Matrix(Matrix):
    '''a class represents a nxn matrix'''

    def __init__(self, dimension):
        '''(Square_Matrix, int) -> None
        This function initializing a square matrix by assigning the dimension
        of it.
        '''
        pass

    def set_diagonal(self, value):
        '''(Square_Matrix, list) -> None
        This function set the value of the diagonal of the matrix.
        If the length of the give list doesn't match the dimension,
        it will raise MatrixNotMatch error.
        '''
        pass

    def get_diagonal(self):
        '''(Square_Matrix) -> list of obj
        This function get the value of the diagonal of the matrix.
        '''
        pass

    def get_determinant(self):
        '''(Square_Matrix) -> int/float
        This function returns the value of the determinant of a 2x2 matrix.
        In any other case, it will raise MatrixNotMatch error.
        '''
        pass

    def swap_row_n_col(self, row_num, col_num):
        '''(Matrix, int, int) -> None
        This function mutate the list by interchanging a row with a colunm in
        a nxn matrix. Otherwise, it will raise MatrixNotMatch error.
        '''    


class One_Dimension_Matrix(Matrix):
    ''' This class represent a 1xn or nx1 matrix.'''

    def __init__(self, num_row, num_col):
        '''(One_Dimension_Matrix) -> None
        This function initializing the one-d matrix by assign the deminsion of
        it.
        '''
        pass

    def get_element(self, element_num):
        '''(One_Dimension_Matrix, int) -> obj
        This function returns the value of list on the given index.
        If list out of range, it will raise MatrixNotMatch error
        '''
        pass


class Symmetric_Matrix(Square_Matrix):
    '''This class represents a symmetric matrix'''

    def __init__(self, dimension):
        '''(Symmetric_Matrix, int) -> None
        This function initializing the matrix by assign the dimension of it
        '''
        pass

    def create(self, value):
        '''(Symmetirc_Matrix, list of list) -> None
        This function set the value of the symmetric matrix by given value.
        '''
        pass


class Indentity_Matrix(Symmetric_Matrix):
    '''This class represents an identity matrix'''

    def __init__(self, dimension):
        '''(Identity_Matrix, int) -> None
        This function initializing the identity matirx by assign the dimension
        of it
        '''
        pass

    def set_diagonal(self, value):
        '''(Square_Matrix, int) -> None
        This function set the value of the diagonal of the identity matrix.
        Except the diagonal, anything else in the matrix is 0.
        '''
        pass


class MatrixNotMatch(Exception):
    pass


class ColNotExist(Exception):
    pass


class RowNotExist(Exception):
    pass
