import itertools

__author__ = 'Gabo'

import unittest


def changeAmount(amount, coins):
    changeList = list()
    if coins:
        if(amount > 0):
            for coin in coins:
                if amount%coin == 0:
                    changeList.append([amount//coin, coin])
            currCoin = coins[0]
            tailCoins = coins[1:]
            if tailCoins:
                    for coin in tailCoins:
                        coinCounter = 1
                        newAmount = amount - coin
                        while(newAmount > 0):
                            if newAmount > 0 and newAmount % currCoin == 0:
                                changeList.append([[newAmount // currCoin, currCoin], [coinCounter, coin]])
                            coinCounter += 1
                            newAmount = newAmount - coin

                            # innerNewAmout = (amount - coin)
                            # if innerNewAmout > 0 and innerNewAmout % currCoin == 0:
                            #     changeList.append([[innerNewAmout // currCoin, currCoin],
                            #                [1, coin]])

    return changeList


class GiveChangeTest(unittest.TestCase):
    def test_noAmount(self):
        self.assertEqual(changeAmount(0, [1, 2]),list())

    def test_noCoins(self):
        self.assertEqual(changeAmount(5, list()),list())

    def test_onePeso(self):
        self.assertEqual(changeAmount(2, [1]),[[2, 1]])
        self.assertEqual(changeAmount(10, [1]),[[10, 1]])

    def test_sameAmount_coin(self):
        self.assertEqual(changeAmount(1, [1]),[[1, 1]])
        self.assertEqual(changeAmount(2, [2]),[[1, 2]])
        self.assertEqual(changeAmount(5, [5]),[[1, 5]])
        self.assertEqual(changeAmount(10, [10]),[[1, 10]])

    def test_2Pesos(self):
        self.assertEqual(changeAmount(1, [2]),[])
        self.assertEqual(changeAmount(3, [2]),[])
        self.assertEqual(changeAmount(4, [2]),[[2, 2]])
        self.assertEqual(changeAmount(16, [2]),[[8, 2]])

    def test_3Pesos(self):
        self.assertEqual(changeAmount(1, [3]),[])
        self.assertEqual(changeAmount(3, [3]),[[1, 3]])
        self.assertEqual(changeAmount(5, [3]),[])
        self.assertEqual(changeAmount(6, [3]),[[2, 3]])
        self.assertEqual(changeAmount(9, [3]),[[3, 3]])

    def test_OneTwoPesos(self):
        self.assertEqual(changeAmount(1, [1,2]),[[1, 1]])
        self.assertEqual(changeAmount(2, [1,2]),[[2, 1], [1,2]])
        self.assertEqual(changeAmount(3, [1,2]),[[3, 1], [[1,1], [1,2]]])
        self.assertEqual(changeAmount(4, [1,2]),[[4, 1], [2,2], [[2,1], [1,2]]])
        self.assertEqual(changeAmount(5, [1,2]),[[5, 1], [[3,1], [1, 2]], [[1,1], [2, 2]]])
        self.assertEqual(changeAmount(6, [1,2]),[[6, 1], [3,2], [[4,1], [1, 2]], [[2,1], [2, 2]]])

    def test_OneThreePesos(self):
        self.assertEqual(changeAmount(1, [1,3]), [[1, 1]])
        self.assertEqual(changeAmount(2, [1,3]), [[2, 1]])
        self.assertEqual(changeAmount(3, [1,3]), [[3, 1], [1, 3]])
        self.assertEqual(changeAmount(4, [1,3]), [[4, 1], [[1, 1], [1, 3]] ])
        self.assertEqual(changeAmount(9, [1,3]), [[9, 1],[3, 3], [[6, 1], [1, 3]], [[3, 1], [2, 3]] ])
        self.assertEqual(changeAmount(10, [1,3]), [[10, 1], [[7, 1], [1, 3]], [[4, 1], [2, 3]], [[1, 1], [3, 3]] ])


    def test_One_Two_ThreePesos(self):
        self.assertEqual(changeAmount(1, [1,2,3]), [[1, 1]])
        self.assertEqual(changeAmount(2, [1,2,3]), [[2, 1], [1, 2]])
        self.assertEqual(changeAmount(3, [1,2,3]), [[3, 1], [1, 3], [[1,1], [1, 2]]])
        self.assertEqual(changeAmount(4, [1,2,3]), [[4, 1], [2, 2], [[2,1], [1,2]], [[1, 1], [1, 3]] ])
        self.assertEqual(changeAmount(5, [1,2,3]), [[5, 1], [[3,1], [1,2]], [[1,1], [2,2]], [[2, 1], [1, 3]]],
                         [[1,2], [1,3]])
        self.assertEqual(changeAmount(6, [1,2,3]), [[6, 1], [3, 2], [2, 3], [[4,1], [1,2]], [[2,1], [2,2]], [[3,1], [1,3]]])
        self.assertEqual(changeAmount(13, [1,2,3]), [[13, 1], [[11,1], [1,2]], [[9,1], [2,2]], [[7,1], [3,2]], [[5,1], [4,2]],
                         [[3,1], [5,2]], [[1,1], [6,2]], [[10,1], [1,3]], [[7,1], [2,3]], [[4,1], [3,3]], [[1,1], [4,3]],
                                                     [[3, 3], [2,2]], [[1, 3], [5,2]] ])

if __name__ == '__main__':
    unittest.main()