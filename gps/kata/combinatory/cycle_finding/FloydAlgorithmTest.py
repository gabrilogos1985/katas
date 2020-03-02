__author__ = 'Gabo'

import unittest


def hasLoop(way, tortoise, hare):
    if tortoise and hare:
        nextHare = hareJump(hare, way)
        next = way.get(tortoise)
        return True if next and nextHare == next else hasLoop(way, next, nextHare)
    return False


def hareJump(hare, way):
    nextHare = way.get(hare) if hare else None
    if nextHare: nextHare = way.get(nextHare)
    return nextHare


class FloyCycleDectectorTest(unittest.TestCase):

    def test_oneStep_linear(self):
        way = {1: None}
        self.assertFalse(hasLoop(way, 1, 1))

    def test_twoStep_linear(self):
        way = {1: 2, 2: None}
        self.assertFalse(hasLoop(way, 1, 1))

    def test_oneStep_Cycle(self):
        way = {1: 1}
        self.assertTrue(hasLoop(way, 1, 1))

    def test_twoStep_Cycle(self):
        way = {1: 2, 2: 1}
        self.assertTrue(hasLoop(way, 1, 1))

    def test_oneLinear_oneStep_Cycle(self):
        way = {1: 2, 2: 2}
        self.assertTrue(hasLoop(way, 1, 1))

    def test_oneLinear_twoStep_Cycle(self):
        way = {1: 2, 2: 3, 3: 2}
        self.assertTrue(hasLoop(way, 1, 1))

    def test_twoLinear_oneStep_Cycle(self):
        way = {1: 2, 2: 3, 3: 3}
        self.assertTrue(hasLoop(way, 1, 1))

if __name__ == '__main__':
    unittest.main()