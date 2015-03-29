from gps.kata.primefactors.PrimeFactorsV2 import PrimerFactorsV2

__author__ = 'Sony'

import unittest


class PrimeFactorTest(unittest.TestCase):
    def test_One(self):
        self.verifyFactors([], 1)

    def test_Two(self):
        self.verifyFactors([2], 2)

    def test_Three(self):
        self.verifyFactors([3], 3)

    def test_11(self):
        self.verifyFactors([11], 11)

    def test_MadeOf2(self):
        self.verifyFactors([2, 2], 4)
        self.verifyFactors([2, 2, 2], 8)

    def test_TwoAndThreeFactors(self):
        self.verifyFactors([2, 3], 6)
        self.verifyFactors([2, 2, 3], 12)

    def test_Nine(self):
        self.verifyFactors([3, 3], 9)

    def test_Ten(self):
        self.verifyFactors([2, 5], 10)

    def test_LongPrimes(self):
        self.verifyFactors([3203431780337], 3203431780337)

    def verifyFactors(self, expectedFactors, number):
        self.assertEqual(expectedFactors, PrimerFactorsV2.generate(number))


if __name__ == '__main__':
    unittest.main()
