import numpy as np
import unittest
from užduotis3.polynomial_doctest import Polynomial

class TestPolynomial(unittest.TestCase):
    def test_cartessian_product(self):
        np.testing.assert_array_equal(Polynomial().cartessian_product(np.arange(2), np.arange(3)),
                         np.array([[0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2]]))
        np.testing.assert_array_equal(Polynomial().cartessian_product(np.array([0, 2]), np.array([1, 3])),
                                      np.array([[0, 1], [2, 1], [0, 3], [2, 3]]))

    def test_multiplication(self):
        product = Polynomial(np.array([0,1]), np.array([1,1])) * Polynomial(np.array([0,1,2]), np.array([1,1,1]))
        self.assertEqual(product, Polynomial(np.array([0, 1, 2, 3]), np.array([1, 2, 2, 1])))

if __name__ == '__main__':
    unittest.main()