__author__ = 'Gabo'

import unittest


def changeAmount(amount, coins):
    changeList = list()
    if coins:
        if(amount > 0):
            for coin in coins:
                if amount%coin == 0:
                    changeList.append([amount//coin, coin])
    return changeList


class GiveChangeTest(unittest.TestCase):
    def test_noAmount(self):
        self.assertEqual(changeAmount(0, [1, 2]),list())

    def test_noCoins(self):
        self.assertEqual(changeAmount(5, list()),list())

    def test_one(self):
        self.assertEqual(changeAmount(1, [1]),[[1, 1]])

    def test_five(self):
        self.assertEqual(changeAmount(5, [5]),[[1, 5]])

    def test_two_1Peso(self):
        self.assertEqual(changeAmount(2, [1]),[[2, 1]])

    def test_two_1Peso(self):
        self.assertEqual(changeAmount(10, [1]),[[10, 1]])

if __name__ == '__main__':
    unittest.main()