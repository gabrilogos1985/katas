from gps.kata.zigzagMatrix.ZigZagMatrix import ZigzagMatrix

__author__ = 'Sony'

import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(["1,1"], ZigzagMatrix.sort(1))

    def test_Two(self):
        self.assertEqual("1,1;1,2;2,1;2,2".split(";"), ZigzagMatrix.sort(2))

    def test_Three(self):
        self.assertEqual("1,1;1,2;2,1;3,1;2,2;1,3;2,3;3,2;3,3".split(";"), ZigzagMatrix.sort(3))

    def test_Four(self):
        self.assertEqual("1,1;1,2;2,1;3,1;2,2;1,3;1,4;2,3;3,2;4,1;4,2;3,3;2,4;3,4;4,3;4,4".split(";"),
                         ZigzagMatrix.sort(4))

    def test_Five(self):
        self.assertEqual(
            "1,1;1,2;2,1;3,1;2,2;1,3;1,4;2,3;3,2;4,1;5,1;4,2;3,3;2,4;1,5;2,5;3,4;4,3;5,2;5,3;4,4;3,5;4,5;5,4;5,5".split(
                ";"),
            ZigzagMatrix.sort(5))

    def test_Six(self):
        self.assertEqual(
            "1,1;1,2;2,1;3,1;2,2;1,3;1,4;2,3;3,2;4,1;5,1;4,2;3,3;2,4;1,5;1,6;2,5;3,4;4,3;5,2;6,1;6,2;5,3;4,4;3,5;2,6"
            ";3,6;4,5;5,4;6,3;6,4;5,5;4,6;5,6;6,5;6,6".split(";"),
            ZigzagMatrix.sort(6))

    def test_printOrderedMatrix(self):
        size = 11
        list = ZigzagMatrix.sort(size)
        for row in range(1, size + 1):
            for colum in range(1, size + 1):
                counter = 1
                for element in list:
                    if element == str(row) + "," + str(colum):
                        print('{:^5}'.format(str(counter)), end='')
                        break
                    counter += 1;
            print('')

if __name__ == '__main__':
    unittest.main()
