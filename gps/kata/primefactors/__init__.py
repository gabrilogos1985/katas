from gps.kata.primefactors.PrimerFactors import PrimerFactors

__author__ = 'Sony'

import unittest


class TestSequenceFunctions(unittest.TestCase):
    def test_numberOne(self):
        list = PrimerFactors.generate(1)
        self.assertEqual(list, [], 'no prime factors')

    def test_factorsOfTwo(self):
        primeFactors = PrimerFactors.generate(4)
        expectedPrimes = [2, 2]
        self.assertEqual(primeFactors, expectedPrimes)
        primeFactors = PrimerFactors.generate(8)
        self.assertEqual(primeFactors, [2, 2, 2])
        primeFactors = PrimerFactors.generate(16)
        self.assertEqual(primeFactors, [2, 2, 2, 2])

    def test_factorsOf3(self):
        self.assertEqual(PrimerFactors.generate(9), [3, 3])
        self.assertEqual(PrimerFactors.generate(27), [3, 3, 3])
        self.assertEqual(PrimerFactors.generate(81), [3, 3, 3, 3])

    def test_factorsOf3And2(self):
        self.assertEqual(PrimerFactors.generate(6), [2, 3])
        self.assertEqual(PrimerFactors.generate(12), [2, 2, 3])

    def test_factorsOf2And3And5(self):
        self.assertEqual(PrimerFactors.generate(10), [2, 5])
        self.assertEqual(PrimerFactors.generate(30), [2, 3, 5])


if __name__ == '__main__':
    unittest.main()
