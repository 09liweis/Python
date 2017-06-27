import unittest
from a1_design import *

class Test(unittest.TestCase):

      def test_1_Matrix_get_row(self):
            a = [[1,2,3], [3,4,5]]
            a = Matrix(2,3)
            a.set_row(a)
            result = a.get_row(1)
            expect = [1,2,3]
            self.assertEqual(result, expect)

      def test_2_Matrix_set_row(self):
            matrix_list = [[1,2,3], [4,5,6]]
            matrix1 = Matrix(2,3)
            matrix1.set_row(matrix_list)
            result = matrix1.get_matrix()
            expect = [[1,2,3], [4,5,6]]
            self.assertEqual(result, expect)

      def test_3_Matrix_get_col(self):
            matrix_list = [[1,2,3], [4,5,6]]
            matrix1 = Matrix(2,3)
            matrix1.set_matrix(matrix_list)
            result = matrix1.get_col(1)
            expect = [[1, 4]]
            self.assertEqual(result, expect)

      def test_4_Matrix_set_col(self):
            matrix_list = [[1,2,3], [4,5,6]]
            matrix1 = Matrix(3,2)
            matrix1.set_col(matrix_list)
            result = matrix1.get_matrix()
            expect = [[1,4], [2, 5], [3,6]]
            self.assertEqual(result, expect)

      def test_5_Matrix_multiply(self):
            list1 = [[1,2,3], [4,5,6]]
            list2 = [[1,2], [3,4], [5,6]]
            matrix1 = Matrix(2,3)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(3, 2)
            matrix2.set_matrix(list2)
            result = matrix1.multiply(matrix2)
            expected = [[22, 28], [49, 64]]
            self.assertEqual(result, expect)

      def test_6_Matrix_multiply_matrix_not_match(self):
            list1 = [[1,2,3], [4,5,6]]
            matrix1 = Matrix(2,3)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(2, 3)
            matrix2.set_matrix(list1)
            result = matrix1.multiply(matrix2)
            self.assertRaises(MatrixNotMatch, result.get_matrix())

      def test_7_Matrix_add_number(self):
            list1 = [[1,2,3], [4,5,6]]
            list2 = [[1,2,3] [4,5,6]]
            matrix1 = Matrix(2,3)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(2, 3)
            matrix2.set_matrix(list2)
            result = matrix1.add(matrix2)
            expected = [[2, 4, 6], [8, 10, 12]]
            self.assertEqual(result.get_matrix(), expect)  

      def test_8_Matrix_add_str(self):
            list1 = [['qw', 'as'], ['zx', 'qw']]
            matrix1 = Matrix(2,2)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(2, 2)
            matrix2.set_matrix(list2)
            result = matrix1.add(matrix2)
            expected = [['qwqw', 'asas'], ['zxzx', 'qwqw']]
            self.assertEqual(result.get_matrix(), expect)

      def test_9_Matrix_add_matrix_not_match(self):
            list1 = [[1,2,3], [4,5,6]]
            list2 = [[1,2,3] [4,5,6], [1,2,3]]
            matrix1 = Matrix(2,3)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(3, 3)
            matrix2.set_matrix(list2)
            result = matrix1.add(matrix2)
            self.assertRaises(MatrixNotMatch, result)        

      def test_10_Matrix_substract(self):
            list1 = [[1,2,3], [4,5,6]]
            matrix1 = Matrix(2,2)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(2, 2)
            matrix2.set_matrix(list2)
            result = matrix1.substract(matrix2)
            expect = [[0,0,0], [0,0,0]]
            self.assertEqual(expect, result.get_matrix())       

      def test_11_Matrix_substract_matrix_not_match(self):
            list1 = [[1,2,3], [4,5,6]]
            list2 = [[1], [2]]
            matrix1 = Matrix(2,2)
            matrix1.set_matrix(list1)
            matrix2 = Matrix(2, 1)
            matrix2.set_matrix(list2)
            result = matrix1.substract(matrix2)
            self.assertRaises(MatrixNotMatch, result)       

      def test_12_Matrix_transpose(self):
            list1 = [[1, 2, 3], [4, 5, 6]]
            matrix = Matrix(2, 3)
            matrix.set_matrix(list1)
            matrix.transpose()
            result = matrix.get_matrix()
            expected = [[1, 4], [2, 5], [3, 6]]
            self.assertEqual(expected, result)

      def test_12_Matrix_transpose_empty(self):
            list1 = [[]]
            matrix = Matrix(0, 0)
            matrix.set_matrix(list1)
            matrix.transpose()
            result = matrix.get_matrix
            expected = [[]]
            self.assertEqual(expected, result)

      def test_12_Matrix_transpose_square_matrix(self):
            list1 = [[1, 2, 3], [4, 5, 6], [1, 2, 3]]
            matrix = Matrix(3, 3)
            matrix.set_matrix(list1)
            matrix.transpose()
            result = matrix.get_matrix()
            expected = [[1, 4, 1], [2, 5, 2], [3, 6, 3]]
            self.assertEqual(expected, result)

      def test_13_Matrix_swap_row(self):
            list1 = [[1, 2, 3], [4, 5, 6]]
            matrix = Matrix(2, 3)
            matrix.set_matrix(list1)
            matrix.swap_row(1, 2)
            result = matrix.get_matrix()
            expected = [[4, 5, 6], [1, 2, 3]]
            self.assertEqual(expected, result)

      def test_13_Matrix_swap_col(self):
            list1 = [[1, 2, 3], [4, 5, 6]]
            matrix = Matrix(2, 3)
            matrix.set_matrix(list1)
            matrix.swap_col(1, 2)
            result = matrix.get_matrix()
            expected = [[2, 1, 3], [5, 4, 6]]
            self.assertEqual(expected, result)
      
      def test_Square_Matrix_determinate(self):
            list1 = [[1, 2], [4, 5]]
            matrix = Square_Matrix(2)
            matrix.set_matrix(list1)
            det = matrix.get_determinant()
            expected = -1
            self.assertEqual(det, expected)
            


unittest.main(exit=False)            