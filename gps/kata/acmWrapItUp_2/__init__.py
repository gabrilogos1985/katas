from gps.kata.acmWrapItUp_2.BookWrapper import BookWrapper

__author__ = 'gabe'

import unittest


class TestSequenceFunctions(unittest.TestCase):
    bookWrapper= BookWrapper()
    def test_oneDimensionSizeOne(self):
        minLenght = self.bookWrapper.wrapItUp([[1,1,1],[1,1,1]])
        self.assertEqual(minLenght,81)
        minLenght = self.bookWrapper.wrapItUp([[1,1,1],[1,1,1],[1,1,0]])
        self.assertEqual(minLenght,81)
        minLenght = self.bookWrapper.wrapItUp([[1,1,1]]*21)
        self.assertEqual(minLenght,81)

    def test_height2Width1Nothickness(self):
        minLenght = self.bookWrapper.wrapItUp([[2,1,0]])
        self.assertEqual(minLenght,82)

    @unittest.skip("solve later medium level case ")
    def test_twoDimensionSizeOne(self):
        minLenght = self.bookWrapper.wrapItUp([1,1,1]*22)
        self.assertEqual(minLenght,83)

    def heightBestThanWith(self):
        pass


if __name__ == '__main__':
    unittest.main()

