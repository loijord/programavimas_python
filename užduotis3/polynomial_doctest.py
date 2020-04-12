import doctest
import numpy as np
import numpy_indexed as npi

class Polynomial:
    '''poynomial instance takes pows and coeffs'''
    def __init__(self, pows=None, coeffs=None):
        self.pows = pows
        self.coeffs = coeffs

    @staticmethod
    def cartessian_product(*arrays):
        """returns cartessian product of several arrays
        >>> Polynomial().cartessian_product(np.arange(2), np.arange(3)).tolist()
        [[0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2]]
        """
        return np.stack(np.meshgrid(*arrays), axis=-1).reshape(-1, len(arrays))

    def __mul__(self, other):
        """ returns product of two polynomials
        >>> P = Polynomial(np.array([0,1]), np.array([1,1])) * Polynomial(np.array([0,1,2]), np.array([1,1,1]))
        >>> print(P.pows)
        [0 1 2 3]
        >>> print(P.coeffs)
        [1 2 2 1]
        """
        cells = self.cartessian_product(self.pows, other.pows) # finding pairs of powers
        powers = np.sum(cells, axis=1) # summation of each pair of powers
        coeffs = self.coeffs[cells[:, 0]] * other.coeffs[cells[:, 1]] # multiplication of corresponding coeffs
        terms = np.column_stack([coeffs, powers]) # result as terms (coeff and power in each row)
        return Polynomial(*npi.group_by(terms[:, 1]).sum(terms[:,0])) # reducing similar terms

    def __eq__(self, other):
        """Implementation of equality
        >>> isinstance(Polynomial(np.array([7]), np.array([8])), Polynomial)
        True
        >>> Polynomial(np.array([7]), np.array([8])) == Polynomial(np.array([7]), np.array([8]))
        True
        """
        if isinstance(other, Polynomial):
            return np.all(np.sort(self.pows) == np.sort(other.pows)) \
                   and np.all(np.sort(self.coeffs) == np.sort(other.coeffs))
        return False


if __name__ == '__main__':
    doctest.testmod(verbose=True)