__author__ = 'Gabo'

import unittest

def count_changePath(money, coins):
    # your implementation here
    coins.sort(reverse=True)
    return get_change(money, coins, [])

def get_change(money, children, path):
    change_ways = find_ways( money, 0, path )    
    if len(children) < 1: return change_ways
        
    for i in range( len(children) ):
        npath = path.copy()
        npath.append(children[i])    
        change_ways += get_change( money, children[i+1:], npath )    

    return change_ways

def find_ways(money, init, coins):    
    
    if len(coins) == 0 and init == money: return 1
    
    if init > money or len(coins) == 0:
        return 0

    i = 1
    counter = 0
    while init + coins[0] * i <= money:
        counter+=find_ways(money, init + coins[0] * i, coins[1:])
        i+=1
    
    return counter


def count_change(money, coins):
    if money<0:
        return 0
    if money == 0:
        return 1
    if money>0 and not coins:
        return 0
    return count_change(money-coins[0],coins) + count_change(money,coins[1:])


class MoneyChangeMachineTest(unittest.TestCase):

    def test_basic(self):
        self.assertEquals(count_change(4, [1,2]), 3)
        self.assertEquals(count_change(10, [5,2,3]), 4)
        self.assertEquals(count_change(11, [5,7]), 0)


    def test_corner_cases(self):
        self.assertEquals(count_change(98, [3, 14, 8]), 19)
        self.assertEquals(count_change(199, [3, 5, 9, 15]), 760)
        self.assertEquals(count_change(300, [5, 10, 20, 50, 100, 200, 500]), 1022)

        self.assertEquals(count_change(301, [5, 10, 20, 50, 100, 200, 500]), 0)
        self.assertEquals(count_change(419, [2, 5, 10, 20, 50]), 18515)
        self.assertEquals(count_changePath(0, [19, 435, 460]), 1)

        self.assertEqual(count_change(825, [18, 415, 392]), 1)
        self.assertEqual(count_change(1, []), 0)        

if __name__ == '__main__':
    unittest.main()