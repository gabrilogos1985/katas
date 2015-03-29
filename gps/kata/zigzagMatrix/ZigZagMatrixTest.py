from gps.kata.zigzagMatrix.ZigZagMatrix import ZigzagMatrix

__author__ = 'Sony'

import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(["1,1"], ZigzagMatrix.sort(1))

    def test_Two(self):
        self.assertEqual(["1,1;1,2;2,1;2,2"], ZigzagMatrix.sort(2))

    def test_Three(self):
        self.assertEqual(["1,1;1,2;2,1;3,1;2,2;1,3;2,3;3,2;3,3"], ZigzagMatrix.sort(3))

    def test_Four(self):
        self.assertEqual(["1,1;1,2;2,1;3,1;2,2;1,3;1,4;2,3;3,2;4,1;4,2;3,3;2,4;3,4;4,3;4,4"], ZigzagMatrix.sort(4))

    def test_Five(self):
        self.assertEqual(["1,1;1,2;2,1;3,1;2,2;1,3;1,4;2,3;3,2;4,1;5,1;4,2;3,3;2,4;1,5;2,5;3,4;4,3;5,2;5,3;4,4;3,5;4,5;5,4;5,5"], ZigzagMatrix.sort(5))



if __name__ == '__main__':
    unittest.main()
