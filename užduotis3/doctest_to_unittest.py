# Čia yra vienintelis šaltinis, kuris man padėjo perprasti doctestus:
# https://stackoverflow.com/questions/5681330/using-doctests-from-within-unittests
import unittest
import doctest
import užduotis3.polynomial_doctest as pl
from užduotis3.polynomial_unittest import TestPolynomial

testSuite = unittest.TestSuite()
testSuite.addTest(unittest.makeSuite(TestPolynomial))
testSuite.addTests(doctest.DocTestSuite(pl))
unittest.TextTestRunner(verbosity = 2).run(testSuite)